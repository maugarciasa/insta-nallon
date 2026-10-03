# Insta Nallon

Marketing do Nallon no Instagram: artes de feed e stories, e Reels.
O código do sistema fica em `C:\dev\Nallon`. Esta pasta guarda só o
planejamento e as peças prontas.

O repositório git é público. Não entram: dado real, credencial, telefone,
material bruto de câmera, áudio de trabalho nem `.mp4` (ver `.gitignore`).

Este arquivo é a fonte única das regras. O `AGENTS.md` só aponta para cá.
Onde outro arquivo divergir deste, vale este. O `docs/prompt-video-nallon.md`
repete as regras de propósito, porque é colado em outra IA: ao mudar uma
regra aqui, refaça o trecho correspondente lá.

## Arquivos

- `docs/guia-artes.md`: prompt padrão do Magnific (estilo fixo, blocos por tipo de peça, regra de custo). Leia antes de gerar qualquer arte.
- `docs/direcao-visual-reels.md`: direção visual obrigatória dos Reels. Leia antes de compor qualquer vídeo.
- `docs/prompt-video-nallon.md`: briefing de Reels para colar em outra IA.
- `planejamento/semana-NN.md`: plano de cada semana (dia, formato, nicho, objetivo, textos e legendas).
- `planejamento/roteiros/<setor>.md`: roteiro de cada Reels.
- `planejamento/registro-videos.md`: uma linha por vídeo feito. Serve para escolher o setor do próximo.
- `artes/semana-NN/`: artes da semana, nome `dia-peça-slide.png` (ex.: `seg-carrossel-02.png`).
- `videos/`: Reels prontos, nome `AAAA-MM-DD-<setor>` (setor em uma palavra: `pdv`, `caixa`, `agenda`…). O git guarda a capa (`.jpg`) e a legenda do post (`.txt`). O `.mp4` fica só na máquina e vai para o Release do mês no GitHub (`reels-AAAA-MM`).
- `amostras-voz/` e `amostras-som/`: áudio de trabalho, fora do git. As trilhas de amostra saem de `trilhas.py`.
- `.claude/skills/reels-nallon/`: skill própria do fluxo diário (`/reels-nallon`). Traz `trilhas.py` (as 5 trilhas ambiente), `producao.md` (regras de produção por cima da `/brag`), `conferir-fala.py` e os `semear-*.sql` das lojas fictícias.
- `.agents/skills/`: cópia da skill para o Codex. Edite só em `.claude/skills/`: o hook de `.githooks/pre-commit` roda `sincronizar-skills.sh` a cada commit, que copia a skill. Em clone novo, ligue o hook uma vez com `git config core.hooksPath .githooks`.

As outras skills de `.claude/skills` e `.agents/skills` são de terceiros,
instaladas com `npx skills`, e ficam fora do git.

## Vídeos: 2 por dia, setores diferentes

1. Leia `planejamento/registro-videos.md` e escolha 2 setores da lista abaixo que ainda não saíram no ciclo atual.
2. Os 2 vídeos do mesmo dia nunca mostram o mesmo setor. Quando der, falam com nichos diferentes.
3. Nenhum setor repete até todos os 16 terem saído. Aí começa um ciclo novo.
4. Cada vídeo mostra um setor só, do gancho ao fecho.
5. Registre cada vídeo em `planejamento/registro-videos.md` assim que ficar pronto.

Vídeo extra (institucional ou de recurso fora da lista, como o Lilo AI
Assistant): só a pedido. Não conta no ciclo nem na cota de 2 por dia. O nome
usa o tema no lugar do setor (`AAAA-MM-DD-lilo`) e o registro marca
"extra" na coluna Setor.

Nichos: AT (assistência técnica), CG (comércio geral), PS (prestadores de
serviço), BAR (barbearias e salões), CLI (clínicas e consultórios, médicos e
odontológicos). O Nallon não é prontuário: para clínica mostra agenda,
clientes, caixa e financeiro.

Setor marcado Pro: a fala e a legenda dizem "no plano Pro".

| # | Setor | O que mostrar | Nicho |
|---|---|---|---|
| 1 | PDV | Bipar produto, F4 para pagar, cupom na hora | CG |
| 2 | Caixa | Abertura, sangria, suprimento, fechamento cego | CG |
| 3 | Ordens de serviço | Status, peças, orçamento, histórico do aparelho | AT |
| 4 | Diagnóstico por IA (Pro) | Sugestão de hipóteses; o técnico revisa e decide | AT |
| 5 | Consulta da OS | Cliente acompanha a OS pelo link público | AT |
| 6 | Estoque e inventário | Estoque baixa sozinho, contagem de inventário | CG |
| 7 | Produtos e serviços | Cadastro, preços, importação de produtos por planilha | CG, PS |
| 8 | Clientes | Cadastro e histórico | todos |
| 9 | Financeiro | Contas a pagar e receber, parcelas, baixas | todos |
| 10 | Crediário (fiado) | Venda parcelada controlada, sem caderno | CG |
| 11 | Compras e fornecedores | Pedido de compra, recebimento, importação da NF-e de entrada pelo XML do fornecedor | CG |
| 12 | Relatórios | Vendas e resultados do período | todos |
| 13 | Dashboard | Visão do dia ao abrir o sistema | todos |
| 14 | Agenda e agendamento online | Link público, cliente marca sozinho | PS |
| 15 | Catálogo online (Pro) | Vitrine pública da loja | CG |
| 16 | Equipe e produtividade | Tarefas e lembretes, busca Ctrl+K, perfis de acesso (Pro) | todos |

## Como fazer cada vídeo

Use a skill `/reels-nallon`: ela escolhe os setores, escreve o roteiro,
chama a `/brag` com as regras do `producao.md` (Reels 1080x1920, narração pt-BR, legenda
sincronizada), copia para `videos/` e registra.

- **Onde rodar.** Tudo o que a `/brag` e o `producao.md` mandam (git, app, Supabase, `brag-output/`) roda dentro de `C:\dev\Nallon`: é lá que ficam o código e o repositório.
- **Tela.** Captura só do app local, com loja fictícia: "Aurora Celulares" para CG e AT, "Barbearia Ponto Certo" para BAR, "Clínica Vida Plena" para CLI e "Ar Frio Climatização" para PS. Cada uma vem de um `semear-*.sql` da `/reels-nallon`. Nunca capture produção nem dados reais.
- **Visual.** Siga `docs/direcao-visual-reels.md`. A legenda nunca fica em cima da interface: o painel termina em y 1240 ou acima e a legenda ocupa a faixa de y 1280 a y 1500, sozinha sobre o fundo.
- **Voz.** Narração sempre com a `narrador` do OmniVoice (perfil em `~/.hyperframes/vozes/narrador/`): voz masculina sintética, criada por descrição. Não troque a voz sem pedido.
- **Trilha.** Música ambiente do primeiro ao último quadro, com uma das 5 trilhas de `trilhas.py`: `1-aurora` (padrão), `2-vidro`, `3-pulso`, `4-manha`, `5-horizonte`. Todas resolvem na tônica nos últimos segundos, junto com a assinatura.
- **Entrega.** Copie `brag.mp4`, `brag.jpg` e `share-copy.txt` para `videos/` com o nome do dia e do setor. Depois do ok, faça o commit da capa, da legenda, do roteiro e do registro, e suba o `.mp4` para o Release do mês.

## Encerramento obrigatório de todo vídeo

Todo vídeo termina com esta assinatura em narração, exatamente assim, sem
alterar, abreviar nem variar:

**"Nallon. Gestão inteligente para o seu negócio."**

- Tom profissional, seguro, moderno e natural. Sem leitura acelerada; pausa curta depois de "Nallon".
- Na tela, só a logo do Nallon (ou o nome NALLON) e a mesma frase, centralizadas sobre o fundo creme. A interface sai aos poucos antes. Sem celular, título, badge, oferta ou efeito luminoso.
- A marca entra com animação sutil, de 0,8 a 1,5 segundo. A cena dura até a fala terminar.
- Nenhuma frase depois da assinatura. Oferta, "teste grátis" e "link na bio" vão antes dela ou só na legenda do post.

## Regras de conteúdo

- Tudo vem do que o sistema faz hoje. Sem número inventado, depoimento ou cliente fictício apresentado como real. Na dúvida, confira no código ou em `C:\dev\Nallon\docs\ai\reference\modules\`.
- O Nallon não emite nota fiscal. Nota de entrada entra pela importação do XML do fornecedor. A consulta de notas na SEFAZ (MDe) ainda não funciona, porque depende do certificado A1 da loja: não mostre nem cite. Nunca sugira que emite.
- Atalhos do PDV: F4 abre o pagamento, F9 busca produto. Não mostre F2 (sangria) nem F3 (suprimento) como se fosse venda.
- Site: `nallon.com.br`. Teste grátis e planos em `nallon.com.br/planos`. Na legenda do post, escreva "link na bio", porque URL em legenda do Instagram não vira link.
- Oferta: 10 dias grátis, sem cartão, sem fidelidade. Preços: Básico R$ 47,00/mês e Pro R$ 87,00/mês. Na fala, por extenso ("quarenta e sete reais por mês"). Nenhum outro valor vale.
- Só no plano Pro: Lilo AI Assistant, diagnóstico por IA, lembretes automáticos e envio automático pelo WhatsApp, perfis de acesso por função, catálogo online, conciliação bancária e cobrança do crediário em lote. O link de agendamento existe nos dois planos.
- Telefone e WhatsApp de contato não ficam escritos no repositório: no plano, use `[WhatsApp comercial]` e troque na hora de publicar.
- Identidade: âmbar `#e8a33d`, fundo creme `#f5f1ea`, texto `#1a1714`. Títulos em Space Grotesk, texto em Geist.
