# Nallon no Instagram: semana 2

Semana dos dois nichos que ficaram fora da primeira: barbearias e salões, e
clínicas e consultórios. Mesma estrutura da semana 1: três posts no feed,
um por objetivo, e Stories nos outros dias.
Tudo aqui vem do que o sistema faz hoje: sem número, depoimento ou cliente inventado.
As regras de conteúdo e a identidade ficam no `CLAUDE.md`; o estilo das artes, em `docs/guia-artes.md`.

A semana ainda não tem data. Ao agendar, anote aqui a segunda-feira de início.
Antes de fechar os horários, leia os números anotados no fim de `semana-01.md`.

| Dia | Formato | Nicho | Objetivo | Ação pedida | Arquivos | Situação |
|---|---|---|---|---|---|---|
| Seg | Carrossel | Barbearias e salões | Reconhecimento | Comentar e enviar | `seg-carrossel-01` a `07` | Artes prontas |
| Ter | Stories | Barbearias e salões | Reconhecimento | Votar na enquete | `ter-story-enquete` | Arte pronta |
| Qua | Reels | Barbearias e salões | Teste grátis | Link na bio | `videos/AAAA-MM-DD-agenda` | Gerar |
| Qui | Stories | Todos | Teste grátis | Link do teste | `qui-story-pergunta`, `qui-story-teste` | Reaproveitar da semana 1; falta a captura do story 1 |
| Sex | Post único | Clínicas e consultórios | Contato WhatsApp | Chamar no WhatsApp | `sex-post` | Arte pronta |
| Sáb | Stories | Clínicas e consultórios | Contato WhatsApp | Chamar no WhatsApp | `sab-story-prontuario`, `sab-story-whatsapp` | Arte pronta; a outra vem da semana 1 |

As artes ficam em `artes/semana-02/`. Os outros Reels da semana seguem o ciclo de setores, com `/reels-nallon`.

---

## Segunda: carrossel (barbearias e salões)

Lista numerada, como na semana 1: cada slide traz um problema que o dono reconhece. A solução só aparece no slide 6.

**Slide 1 (capa)**
> 4 sinais de que a agenda da sua barbearia não cabe mais no WhatsApp
> (o 2º já te custou um cliente)

**Slide 2 (sinal 1)**
> "Tem horário hoje?"
> E você responde com a máquina na mão.
> Cada resposta atrasada é um cliente que marca em outro lugar.

**Slide 3 (sinal 2)**
> Dois clientes chegam para o mesmo horário.
> Um dos dois vai embora irritado.

**Slide 4 (sinal 3)**
> O cliente esquece e a cadeira fica vazia.
> Horário vazio não volta.

**Slide 5 (sinal 4)**
> No fim do dia, o caixa não bate com os atendimentos.
> E ninguém sabe onde está a diferença.

**Slide 6 (virada)**
> No Nallon, o cliente marca sozinho pelo link: escolhe o serviço, o profissional e o horário livre.
> Agenda, clientes e caixa ficam no mesmo sistema.
> E, no plano Pro, o lembrete vai sozinho pelo WhatsApp.

**Slide 7 (fechamento)**
> Qual desses sinais mais acontece aí?
> Comenta o número 👇
> Manda este post para quem divide a agenda com você.

**Legenda**

```
Agenda no WhatsApp funciona. Até o dia em que dois clientes chegam para o mesmo horário.

Com o Nallon, você manda um link. O cliente escolhe o serviço, o profissional e o horário livre, e o agendamento entra direto na sua agenda.

No plano Pro, o lembrete vai sozinho pelo WhatsApp.

Comenta qual sinal mais acontece aí 👇 e manda este post para o seu sócio.

#nallon #barbearia #agendamentoonline #gestaodebarbearia #salaodebeleza
```

**Texto alternativo:** Carrossel "4 sinais de que a agenda da sua barbearia não cabe mais no WhatsApp", com ilustrações de cadeira de barbeiro, celular e agenda.

---

## Quarta: Reels (barbearias e salões)

Setor Agenda e agendamento online, gerado com `/reels-nallon --setores agenda`, a partir do app local, com a loja fictícia "Barbearia Ponto Certo" (`semear-barbearia.sql`). Duração de 20 a 30 s.
A skill escreve o roteiro final em `planejamento/roteiros/agenda.md`. A tabela abaixo é o ponto de partida.

| Cena | Tela | Fala |
|---|---|---|
| Gancho | Página pública de agendamento aberta no celular | "Seu cliente ainda pergunta se tem horário?" |
| Escolher | Cliente escolhe o serviço e o profissional | "No Nallon, ele abre o link, escolhe o serviço e o profissional…" |
| Marcar | Horários livres, toque em um deles, confirmação | "…e marca sozinho em um horário livre." |
| Resultado | Agenda da barbearia com o agendamento novo | "O horário já aparece na sua agenda." |
| Oferta | Tela do sistema | "Testa dez dias grátis, sem cartão." |
| Encerramento | Logo do Nallon e a assinatura | "Nallon. Gestão inteligente para o seu negócio." |

O link de agendamento existe nos dois planos: a fala não cita plano. Se o roteiro mostrar lembrete automático, a fala diz "no plano Pro".

**Legenda**

```
Seu cliente marca o horário sozinho, sem esperar você responder no WhatsApp.

Ele abre o link, escolhe o serviço, o profissional e o horário livre. O agendamento já aparece na sua agenda.

A partir de R$ 47,00 por mês, sem fidelidade.

👉 10 dias grátis, sem cartão: link na bio.

#nallon #barbearia #agendamentoonline #agendaonline #salaodebeleza
```

---

## Sexta: post único (clínicas e consultórios)

**Arte**
Ilustração em traço de um balcão de recepção com um computador mostrando uma agenda do dia, fundo creme, destaque âmbar e botão "Chama no WhatsApp".

> Texto grande: **A recepção da clínica em um só sistema.**
> Texto menor: Agenda, cadastro e caixa no mesmo lugar.

**Legenda**

```
Agenda em um caderno, cadastro em uma planilha e o caixa em outro papel?

O Nallon junta a agenda dos profissionais, o cadastro dos clientes, o caixa e o financeiro da clínica, direto no navegador.

E o paciente pode marcar sozinho, pelo link de agendamento.

O Nallon não é prontuário eletrônico: ele cuida da gestão da recepção e do financeiro.

Quer ver funcionando na sua clínica? Chama no WhatsApp: link na bio ou [WhatsApp comercial]. Atendimento de segunda a sexta, das 8h às 18h.

#nallon #gestaodeclinica #consultorio #agendaonline #clinicaodontologica
```

A legenda diz que o Nallon não é prontuário para não prometer o que o sistema não faz.

**Texto alternativo:** Ilustração de um balcão de recepção com um computador e a frase "A recepção da clínica em um só sistema".

---

## Stories

**Terça (reconhecimento)**
1. Arte `ter-story-enquete`: "Como seu cliente marca horário hoje?" Enquete: WhatsApp / Ligação / Link.
2. Reposte o carrossel de segunda: "4 sinais. Qual acontece aí?"

**Quinta (teste grátis)**
1. Bastidor: a página pública de agendamento aberta no celular. Texto: "É isso que o seu cliente vê." A captura vem do app local, com a "Barbearia Ponto Certo" (`/agendar/barbearia-ponto-certo`). Nunca de produção.
2. Arte `qui-story-pergunta` da semana 1, com caixa de pergunta: "O que você quer saber sobre o Nallon?"
3. Arte `qui-story-teste` da semana 1, com adesivo de link para `nallon.com.br/planos`: "10 dias grátis, sem cartão".

**Sábado (WhatsApp)**
1. Responda 2 ou 3 perguntas da caixa de quinta.
2. Arte `sab-story-prontuario`: "O Nallon é prontuário?" Resposta: "Não. Ele cuida da agenda, do cadastro, do caixa e do financeiro da clínica."
3. Arte `sab-story-whatsapp` da semana 1, com adesivo de link para o WhatsApp: "Tira sua dúvida com a gente".

Se a caixa de quinta vier vazia, use as perguntas comuns do fim da seção de Stories de `semana-01.md`.

---

## Prompts das artes

Cole o bloco de estilo fixo de `docs/guia-artes.md` e, embaixo, o bloco da peça. Configuração e regra de custo: as do guia.

| Arquivo | Bloco | Textos | Cena |
|---|---|---|---|
| `seg-carrossel-01` | 1. Capa | N "4"; título "sinais de que a agenda da sua barbearia não cabe mais no WhatsApp"; pílula "o 2º já te custou um cliente" | barber chair next to a smartphone full of chat bubbles |
| `seg-carrossel-02` | 2. Interno, número 1 | "“Tem horário hoje?” E você responde com a máquina na mão." / "Cada resposta atrasada é um cliente que marca em outro lugar." | hand holding a hair clipper and a smartphone with a chat bubble |
| `seg-carrossel-03` | 2. Interno, número 2 | "Dois clientes chegam para o mesmo horário." / "Um dos dois vai embora irritado." | two people standing next to one barber chair and a wall clock |
| `seg-carrossel-04` | 2. Interno, número 3 | "O cliente esquece e a cadeira fica vazia." / "Horário vazio não volta." | empty barber chair and a wall clock |
| `seg-carrossel-05` | 2. Interno, número 4 | "No fim do dia, o caixa não bate com os atendimentos." / "E ninguém sabe onde está a diferença." | cash drawer with coins next to a paper notebook |
| `seg-carrossel-06` | 2. Interno, sem número | "No Nallon, o cliente marca sozinho pelo link." / "Agenda, clientes e caixa no mesmo sistema. E, no plano Pro, o lembrete vai sozinho pelo WhatsApp." | smartphone showing a booking calendar with time slots |
| `seg-carrossel-07` | 3. Final | "Qual desses sinais mais acontece aí?"; pílula "Comenta o número" | speech bubble |
| `ter-story-enquete` | 5. Story | "Como seu cliente marca horário hoje?" | smartphone and a paper agenda |
| `sex-post` | 4. Post único | "A recepção da clínica em um só sistema." / "Agenda, cadastro e caixa no mesmo lugar."; pílula "Chama no WhatsApp" | reception desk with a computer showing a daily schedule |
| `sab-story-prontuario` | 5. Story | "O Nallon é prontuário? Não. Ele cuida da agenda, do cadastro, do caixa e do financeiro da clínica." | clipboard and a calendar |

No slide 6 do carrossel o texto de apoio precisa sair inteiro, com "no plano Pro". Confira antes de aceitar a arte.

---

## O que medir no fim da semana

| Objetivo | Peça | Número que importa |
|---|---|---|
| Reconhecimento | Carrossel e enquete | Alcance, salvamentos, envios, comentários e votos |
| Teste grátis | Reels e stories de quinta | Toques no link da bio e no adesivo de link |
| Contato WhatsApp | Post de sexta e stories de sábado | Conversas iniciadas no WhatsApp |

Compare com a semana 1: qual nicho e qual formato renderam mais por objetivo.

---

## Pendências antes de publicar

1. Gerar o Reels de quarta com `/reels-nallon --setores agenda`.
2. Capturar a tela do story 1 de quinta no app local.
3. Na legenda de sexta, trocar `[WhatsApp comercial]` pelo número na hora de publicar.
4. Definir as datas e anotar a segunda-feira de início no topo.
