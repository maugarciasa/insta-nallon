-- Loja fictícia do Nallon para gravar vídeo. Só no Supabase LOCAL:
--   docker exec -i supabase_db_nallon psql -U postgres -d postgres < semear-video.sql
-- Idempotente: se a loja já existe, não faz nada.
-- Login no app local: carlos@video.local / aurora-video-local-2026
-- (credencial sintética; o banco só escuta em 127.0.0.1).
\set ON_ERROR_STOP 1

select not exists (select 1 from public.lojas where nome = 'Aurora Celulares') as vazio \gset
\if :vazio

begin;

insert into public.lojas (nome, slug, plano, segmento, ativa, dados_principais_concluidos_em)
  values ('Aurora Celulares', 'aurora-celulares', 'manual', 'assistencia_tecnica', true, now())
  returning id as loja \gset

with novo as (
  insert into auth.users (instance_id, id, aud, role, email, encrypted_password, email_confirmed_at,
    raw_app_meta_data, raw_user_meta_data, created_at, updated_at,
    confirmation_token, recovery_token, email_change, email_change_token_new)
  values ('00000000-0000-0000-0000-000000000000', extensions.uuid_generate_v4(), 'authenticated', 'authenticated',
    'carlos@video.local', extensions.crypt('aurora-video-local-2026', extensions.gen_salt('bf')), now(),
    jsonb_build_object('provider', 'email', 'providers', jsonb_build_array('email')),
    jsonb_build_object('nome', 'Carlos', 'loja_id', :'loja'), now(), now(), '', '', '', '')
  returning id)
insert into auth.identities (provider_id, user_id, identity_data, provider, created_at, updated_at)
select id::text, id, jsonb_build_object('sub', id::text, 'email', 'carlos@video.local', 'email_verified', true, 'phone_verified', false),
       'email', now(), now() from novo
returning user_id as usuario \gset

set local session_replication_role = replica;

insert into public.usuarios (id, loja_id, perfil_id, nome, email, ativo, telefone)
  values (:'usuario', :loja, (select id from public.perfis where slug = 'admin'), 'Carlos', 'carlos@video.local', true, '11999990000')
  on conflict (id) do update set loja_id = excluded.loja_id, perfil_id = excluded.perfil_id, ativo = true;

insert into public.configuracoes (loja_id, chave, valor) values
  (:loja, 'desconto_maximo_caixa', '10'::jsonb),
  (:loja, 'garantia_servico_dias', '90'::jsonb),
  (:loja, 'fechamento_cego', 'false'::jsonb)
  on conflict (loja_id, chave) do update set valor = excluded.valor;

insert into public.produtos (loja_id, nome, sku, preco_custo, preco_venda) values
  (:loja, 'Película de Vidro 3D', '7891023400011', 8, 25),
  (:loja, 'Cabo USB-C Reforçado 1m', '7891023400028', 12, 35),
  (:loja, 'Carregador Turbo 20W', '7891023400035', 32, 79.90),
  (:loja, 'Capinha Silicone iPhone 13', '7891023400042', 14, 39.90),
  (:loja, 'Fone Bluetooth Pulse', '7891023400059', 58, 129.90),
  (:loja, 'Suporte Veicular Magnético', '7891023400066', 19, 49.90),
  (:loja, 'Cartão de Memória 64GB', '7891023400073', 27, 59.90);

insert into public.estoque_movimentacoes (loja_id, produto_id, tipo, quantidade, observacao, usuario_id)
  select :loja, id, 'entrada', 40, 'Estoque inicial', :'usuario' from public.produtos where loja_id = :loja;

insert into public.servicos (loja_id, nome, descricao, preco) values
  (:loja, 'Troca de bateria', 'Bateria nova com teste de carga', 180),
  (:loja, 'Troca de tela', 'Frontal completa com teste de toque', 350),
  (:loja, 'Limpeza de conector', 'Limpeza do conector de carga', 40),
  (:loja, 'Gravação a laser personalizada', 'Gravação em capinha ou acessório', 30);

insert into public.clientes (loja_id, nome, celular) values
  (:loja, 'Mariana Souza', '11987650001'), (:loja, 'João Pereira', '11987650002'),
  (:loja, 'Ana Lima', '11987650003'), (:loja, 'Rafael Costa', '11987650004'),
  (:loja, 'Beatriz Alves', '11987650005'), (:loja, 'Lucas Martins', '11987650006'),
  (:loja, 'Fernanda Rocha', '11987650007');

insert into public.ordens_servico (loja_id, cliente_id, atendente_id, tecnico_id, equipamento, marca, modelo,
    defeito_relatado, status, status_desde, previsao_entrega, criado_em)
select :loja, c.id, :'usuario', :'usuario', v.equip, v.marca, v.modelo, v.defeito, v.status,
       now() - v.idade, current_date + v.prazo, now() - v.idade
  from (values
    ('Mariana Souza', 'iPhone 13 128GB', 'Apple', 'iPhone 13', 'Bateria descarregando rápido', 'em_execucao', interval '5 hours', 1),
    ('João Pereira', 'Galaxy S22', 'Samsung', 'Galaxy S22', 'Tela trincada após queda', 'pronta', interval '1 day', 0),
    ('Ana Lima', 'Moto G84', 'Motorola', 'Moto G84', 'Não carrega', 'aguardando_diagnostico', interval '40 minutes', 2),
    ('Rafael Costa', 'Redmi Note 13', 'Xiaomi', 'Redmi Note 13', 'Câmera traseira embaçada', 'aguardando_aprovacao', interval '3 hours', 3),
    ('Beatriz Alves', 'iPhone 11', 'Apple', 'iPhone 11', 'Troca de frontal', 'aguardando_peca', interval '2 days', 4),
    ('Lucas Martins', 'Galaxy A54', 'Samsung', 'Galaxy A54', 'Conector de carga com mau contato', 'em_execucao', interval '2 hours', 1),
    ('Fernanda Rocha', 'iPad 9ª geração', 'Apple', 'iPad 9', 'Botão home sem resposta', 'aguardando_diagnostico', interval '20 minutes', 3)
  ) as v(cliente, equip, marca, modelo, defeito, status, idade, prazo)
  join public.clientes c on c.loja_id = :loja and c.nome = v.cliente;

commit;
\echo 'loja semeada:' :loja

\else
\echo 'loja já semeada'
\endif
