# Insta Nallon

Marketing do Nallon no Instagram: artes de feed e stories, e Reels.
O código do sistema fica em `C:\dev\Nallon`. Esta pasta guarda só o
planejamento e as peças prontas. É um repositório git público:
nada de dado real, credencial ou material bruto (fotos e vídeos de câmera
ficam fora, no `.gitignore`).

Este arquivo é a fonte única das regras. O `AGENTS.md` só aponta para cá.

## Arquivos

- `docs/guia-artes.md`: prompt padrão do Magnific (estilo fixo, blocos por tipo de peça, regra de custo). Leia antes de gerar qualquer arte.
- `docs/prompt-video-nallon.md`: briefing de Reels para outra IA.
- `planejamento/semana-NN.md`: plano de cada semana (dia, formato, nicho, objetivo, textos e legendas).
- `planejamento/roteiros/<setor>.md`: roteiro de cada Reels, quando houver.
- `planejamento/registro-videos.md`: um registro por vídeo feito. Serve para escolher o setor do próximo.
- `artes/`: artes geradas, nome `dia-peça-slide.png`.
- `videos/`: Reels prontos, nome `AAAA-MM-DD-<setor>.mp4` (setor em uma palavra: `pdv`, `caixa`, `agenda`…), com `.jpg` (capa) e `.txt` (legenda do post) de mesmo nome.
- `.claude/skills/brag-instagram/`: skill própria que gera os Reels. É a cópia oficial: `~/.claude/skills/brag-instagram` é junction para cá. A de `.agents/skills/` (Codex) é a mesma com `~/.claude/` trocado por `~/.Codex/`; ao editar uma, refazer a outra. As outras skills de `.claude/skills` e `.agents/skills` são de terceiros, instaladas com `npx skills`, e ficam fora do git.

## Vídeos: 2 por dia, setores diferentes

1. Leia `planejamento/registro-videos.md` e escolha 2 setores da lista abaixo que ainda não saíram no ciclo atual.
2. Os 2 vídeos do mesmo dia nunca mostram o mesmo setor. Quando der, falam com nichos diferentes.
3. Nenhum setor repete até todos os 16 terem saído. Aí começa um ciclo novo.
4. Cada vídeo mostra um setor só, do gancho ao fecho.
5. Registre cada vídeo em `planejamento/registro-videos.md` assim que ficar pronto.

Nichos: AT (assistência técnica), CG (comércio geral), PS (prestadores de serviço), BAR (barbearias e salões), CLI (clínicas e consultórios, médicos e odontológicos). O Nallon não é prontuário: para clínica mostra agenda, clientes, caixa e financeiro. O prompt para outra IA está em `prompt-video-nallon.md`.
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

Use a skill `/brag-instagram` (Reels 1080x1920, narração pt-BR com a voz
`minha-voz` do OmniVoice, legenda sincronizada). Rode tudo o que a skill
manda (git, app, Supabase, `brag-output/`) dentro de `C:\dev\Nallon`:
é lá que ficam o código e o repositório. Siga as regras dela: captura
só do app local, com a loja fictícia "Aurora Celulares". Nunca capture
produção nem dados reais.

Terminado o vídeo, copie `brag.mp4`, `brag.jpg` e `share-copy.txt` para
`videos/` com o nome do dia e do setor.

## Encerramento obrigatório de todo vídeo

Todo vídeo termina com esta assinatura em narração, exatamente assim, sem alterar,
abreviar nem variar:

**"Nallon. Gestão inteligente para o seu negócio."**

- Tom profissional, seguro, moderno e natural. Sem leitura acelerada; pausa curta depois de "Nallon".
- Sempre que possível, a assinatura sai junto com a logo da Nallon na tela.
- Encerramento limpo e premium: sem elementos visuais nem informações concorrentes.
- Nenhuma frase depois da assinatura. Oferta, "teste grátis" e "link na bio" vão antes dela ou só na legenda do post.
- A legenda na tela mostra a mesma frase.

## Regras de conteúdo

- Tudo vem do que o sistema faz hoje. Sem número inventado, depoimento ou cliente fictício apresentado como real. Na dúvida, confira no código ou em `C:\dev\Nallon\docs\ai\reference\modules\`.
- O Nallon não emite nota fiscal. Nota de entrada entra pela importação do XML do fornecedor. A consulta de notas na SEFAZ (MDe) ainda não funciona, porque depende do certificado A1 da loja: não mostre nem cite. Nunca sugira que emite.
- Atalhos do PDV: F4 abre o pagamento, F9 busca produto. Não mostre F2 (sangria) nem F3 (suprimento) como se fosse venda.
- Site: `nallon.com.br`. Teste grátis e planos em `nallon.com.br/planos`. Na legenda do post, escreva "link na bio", porque URL em legenda do Instagram não vira link.
- Oferta: 10 dias grátis, sem cartão, sem fidelidade. Preços: Básico R$ 47,00/mês e Pro R$ 87,00/mês. Na fala, por extenso ("quarenta e sete reais por mês"). O valor mudou: o R$ 39,90 antigo não vale mais.
- Só no plano Pro: diagnóstico por IA, lembretes automáticos e envio automático pelo WhatsApp, perfis de acesso por função, catálogo online, conciliação bancária e cobrança do crediário em lote. O link de agendamento existe nos dois planos.
- Identidade: âmbar `#e8a33d`, fundo creme `#f5f1ea`, texto `#1a1714`. Títulos em Space Grotesk, texto em Geist.
