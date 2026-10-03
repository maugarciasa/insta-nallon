-- Clínica fictícia do Nallon para gravar vídeo do nicho CLI (agenda, clientes, caixa, financeiro). Só no Supabase LOCAL:
--   docker exec -i supabase_db_nallon psql -U postgres -d postgres < semear-clinica.sql
-- Idempotente: se a loja já existe, não faz nada.
-- Login no app local: helena@video.local / vida-plena-video-2026
-- (credencial sintética; o banco só escuta em 127.0.0.1).
-- Página pública de agendamento: /agendar/clinica-vida-plena
\set ON_ERROR_STOP 1

select not exists (select 1 from public.lojas where nome = 'Clínica Vida Plena') as vazio \gset
\if :vazio

begin;

insert into public.lojas (nome, slug, plano, segmento, ativa, dados_principais_concluidos_em)
  values ('Clínica Vida Plena', 'clinica-vida-plena', 'manual', 'clinica', true, now())
  returning id as loja \gset

with novo as (
  insert into auth.users (instance_id, id, aud, role, email, encrypted_password, email_confirmed_at,
    raw_app_meta_data, raw_user_meta_data, created_at, updated_at,
    confirmation_token, recovery_token, email_change, email_change_token_new)
  values ('00000000-0000-0000-0000-000000000000', extensions.uuid_generate_v4(), 'authenticated', 'authenticated',
    'helena@video.local', extensions.crypt('vida-plena-video-2026', extensions.gen_salt('bf')), now(),
    jsonb_build_object('provider', 'email', 'providers', jsonb_build_array('email')),
    jsonb_build_object('nome', 'Helena', 'loja_id', :'loja'), now(), now(), '', '', '', '')
  returning id)
insert into auth.identities (provider_id, user_id, identity_data, provider, created_at, updated_at)
select id::text, id, jsonb_build_object('sub', id::text, 'email', 'helena@video.local', 'email_verified', true, 'phone_verified', false),
       'email', now(), now() from novo
returning user_id as usuario \gset

set local session_replication_role = replica;

insert into public.usuarios (id, loja_id, perfil_id, nome, email, ativo, telefone)
  values (:'usuario', :loja, (select id from public.perfis where slug = 'admin'), 'Helena', 'helena@video.local', true, '11999990001')
  on conflict (id) do update set loja_id = excluded.loja_id, perfil_id = excluded.perfil_id, ativo = true;

insert into public.servicos (loja_id, nome, descricao, preco, duracao_minutos, agendamento_online) values
  (:loja, 'Consulta', 'Primeira consulta', 180, 30, true),
  (:loja, 'Retorno', 'Retorno em até 30 dias', 90, 30, true),
  (:loja, 'Limpeza dental', 'Profilaxia completa', 200, 60, true),
  (:loja, 'Avaliação odontológica', 'Avaliação e plano de tratamento', 120, 30, true);

insert into public.recursos_agenda (loja_id, nome, tipo, usuario_id, publico) values
  (:loja, 'Dra. Helena', 'profissional', :'usuario', true),
  (:loja, 'Dr. Marcos', 'profissional', null, true),
  (:loja, 'Dra. Paula', 'profissional', null, true);

insert into public.servicos_recursos_agenda (loja_id, servico_id, recurso_id, obrigatorio)
  select :loja, s.id, r.id, false from public.servicos s cross join public.recursos_agenda r
   where s.loja_id = :loja and r.loja_id = :loja;

-- segunda (1) a sexta (5), 8h às 18h, por profissional
insert into public.disponibilidades_agenda (loja_id, recurso_id, dia_semana, inicio, fim)
  select :loja, r.id, d, time '08:00', time '18:00'
    from public.recursos_agenda r cross join generate_series(1, 5) d where r.loja_id = :loja;

insert into public.configuracoes_agenda (loja_id, agendamento_publico_ativo, permitir_escolher_profissional, mostrar_preco,
    intervalo_slots_minutos, antecedencia_minima_minutos, lembretes_automaticos)
  values (:loja, true, true, true, 30, 30, false)
  on conflict (loja_id) do update set agendamento_publico_ativo = true, permitir_escolher_profissional = true,
    mostrar_preco = true, intervalo_slots_minutos = 30, antecedencia_minima_minutos = 30;

insert into public.clientes (loja_id, nome, celular) values
  (:loja, 'Camila Duarte', '11987650021'), (:loja, 'Roberto Nunes', '11987650022'),
  (:loja, 'Patrícia Moraes', '11987650023'), (:loja, 'Eduardo Farias', '11987650024'),
  (:loja, 'Juliana Prado', '11987650025'), (:loja, 'Sérgio Tavares', '11987650026');

-- agenda de hoje e de amanhã (fuso de São Paulo)
with base as (select (now() at time zone 'America/Sao_Paulo')::date as hoje),
ag as (
  select * from (values
    ('Camila Duarte', 'Limpeza dental', 'Dra. Helena', 0, '15:00', 'confirmado', 'publico'),
    ('Roberto Nunes',    'Consulta', 'Dr. Marcos', 0, '15:00', 'agendado', 'publico'),
    ('Eduardo Farias',   'Consulta', 'Dra. Helena', 0, '16:30', 'agendado', 'interno'),
    ('Juliana Prado',  'Retorno', 'Dra. Paula', 0, '16:00', 'confirmado', 'publico'),
    ('Patrícia Moraes','Limpeza dental', 'Dr. Marcos', 0, '16:30', 'agendado', 'publico'),
    ('Sérgio Tavares',   'Avaliação odontológica', 'Dra. Paula', 0, '17:30', 'agendado', 'interno'),
    ('Camila Duarte', 'Retorno', 'Dra. Helena', 1, '10:00', 'agendado', 'publico'),
    ('Roberto Nunes',    'Consulta', 'Dr. Marcos', 1, '11:00', 'confirmado', 'publico')
  ) as t(cliente, servico, prof, dia, hora, status, origem)
),
novos as (
  insert into public.agendamentos (loja_id, cliente_id, servico_id, inicio, fim, status, origem, criado_por)
  select :loja, c.id, s.id,
         ((b.hoje + a.dia) + a.hora::time) at time zone 'America/Sao_Paulo',
         ((b.hoje + a.dia) + a.hora::time + make_interval(mins => s.duracao_minutos)) at time zone 'America/Sao_Paulo',
         a.status, a.origem, :'usuario'
    from ag a cross join base b
    join public.clientes c on c.loja_id = :loja and c.nome = a.cliente
    join public.servicos s on s.loja_id = :loja and s.nome = a.servico
  returning id, cliente_id, servico_id, inicio, fim
)
insert into public.agendamento_alocacoes (loja_id, agendamento_id, recurso_id, inicio, fim)
  select :loja, n.id, r.id, n.inicio, n.fim
    from novos n
    join public.clientes c on c.id = n.cliente_id
    join ag a on a.cliente = c.nome and n.inicio = ((select hoje from base) + a.dia + a.hora::time) at time zone 'America/Sao_Paulo'
    join public.recursos_agenda r on r.loja_id = :loja and r.nome = a.prof;

commit;
\echo 'clínica semeado:' :loja

\else
\echo 'clínica já semeado'
\endif
