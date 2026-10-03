# Insta Nallon

Planejamento e peças do Instagram do [Nallon](https://nallon.com.br), sistema
de gestão web para negócios que vendem no balcão ou atendem com hora marcada:
comércio, assistência técnica, barbearias e salões, clínicas e prestadores de
serviço.

O código do sistema fica em outro repositório. Aqui ficam só o plano de
conteúdo, os roteiros, as artes e os Reels prontos.

## Estrutura

| Caminho | Conteúdo |
|---|---|
| `CLAUDE.md` | Regras do projeto: setores, ciclo de vídeos, regras de conteúdo e identidade. Fonte única. |
| `AGENTS.md` | Aponta para o `CLAUDE.md`. |
| `docs/guia-artes.md` | Prompt padrão das artes (estilo fixo e blocos por tipo de peça). |
| `docs/direcao-visual-reels.md` | Direção visual dos Reels: formato, interface, legenda, movimento e encerramento. |
| `docs/prompt-video-nallon.md` | Briefing completo de Reels para colar em outra IA. |
| `planejamento/semana-NN.md` | Plano de cada semana: formato, nicho, textos e legendas. |
| `planejamento/roteiros/` | Roteiro de cada Reels. |
| `planejamento/registro-videos.md` | Vídeos feitos, por setor, para escolher o próximo. |
| `artes/semana-NN/` | Artes finais de feed e stories (`dia-peça-slide.png`). |
| `videos/` | Capa (`.jpg`) e legenda (`.txt`) de cada Reels, nome `AAAA-MM-DD-<setor>`. |
| `.claude/skills/reels-nallon/` | Skill do fluxo diário: `/reels-nallon` escolhe os 2 setores, gera os vídeos, registra e versiona. Inclui as trilhas ambiente próprias (`trilhas.py`). |
| `.claude/skills/brag-instagram/` | Skill que gera cada Reels a partir do app local, com dados fictícios. |
| `.agents/skills/` | Cópia das duas skills para o Codex, gerada por `sincronizar-skills.sh`. |

Os `.mp4` não ficam no git. Cada Reels final vai para o
[Release](https://github.com/maugarciasa/insta-nallon/releases) do mês
(`reels-AAAA-MM`).

## Como os Reels são feitos

A skill `/brag-instagram` grava o app rodando localmente com uma loja
fictícia ("Aurora Celulares" ou a barbearia de demonstração), narra em pt-BR e
sincroniza a legenda. A música de fundo é sintetizada por `trilhas.py`
(só `numpy`), sem faixa de terceiros.

A skill depende de skills de terceiros que não estão neste repositório.
Instale com `npx skills add <repositório>`:

- [`latent-spaces/brag`](https://github.com/latent-spaces/brag): `/brag`, base da `/brag-instagram`.
- [`heygen-com/hyperframes`](https://github.com/heygen-com/hyperframes): composição, render, áudio e legenda.
- [`coreyhaines31/marketingskills`](https://github.com/coreyhaines31/marketingskills): copywriting, social, content-strategy e marketing-ideas.
- [`petergyang/no-ai-slop`](https://github.com/petergyang/no-ai-slop): revisão de texto.

As credenciais nos arquivos `.sql`
da skill são sintéticas e só valem no Supabase local (`127.0.0.1`).

## Regras que todo conteúdo segue

- Só o que o sistema faz hoje: sem número, depoimento ou cliente inventado.
- Nenhum dado real na tela.
- Todo vídeo termina com "Nallon. Gestão inteligente para o seu negócio."
- Identidade: âmbar `#e8a33d`, creme `#f5f1ea`, texto `#1a1714`; Space Grotesk e Geist.

## Direitos

Marca, textos, artes e vídeos são do Nallon. Todos os direitos reservados.
O repositório é público para consulta; o conteúdo não tem licença de reuso.
