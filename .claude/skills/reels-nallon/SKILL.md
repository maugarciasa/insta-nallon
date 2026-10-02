---
name: reels-nallon
description: Produz os Reels do dia do Nallon de ponta a ponta. Escolhe 2 setores pelo ciclo do registro, gera cada vídeo com a /brag-instagram e a trilha ambiente própria, copia para videos/, registra e faz o commit. Use quando o usuário disser "/reels-nallon", "vídeos do dia", "faz os reels de hoje" ou "próximos vídeos do Nallon".
---

# /reels-nallon

Fluxo diário do projeto Insta Nallon (`C:\dev\Insta Nallon`). As regras de
conteúdo, a lista dos 16 setores e o encerramento obrigatório ficam no
`CLAUDE.md` da raiz desse projeto. Leia esse arquivo inteiro antes do passo 1.
Onde este arquivo e o `CLAUDE.md` divergirem, vale o `CLAUDE.md`.

`<skill-dir>` é a pasta deste `SKILL.md`. `<projeto>` é `C:\dev\Insta Nallon`.

## Opções

| Opção | Padrão |
|---|---|
| `--setores <a>,<b>` | os 2 escolhidos no passo 1 |
| `--um` | só 1 vídeo em vez de 2 |
| `--trilha <1-5>` | `1` (pad calmo, o dos vídeos já publicados) |
| `--data AAAA-MM-DD` | hoje |
| `--voz`, `--sem-voz`, `--no-music`, `--no-sfx` | repassadas à `/brag-instagram` |

Trilhas, geradas por `<skill-dir>/trilhas.py`:

| # | Arquivo | Clima |
|---|---|---|
| 1 | `1-pad-atual` | pad calmo, um pouco melancólico |
| 2 | `2-pad-claro` | pad em tom maior, otimista |
| 3 | `3-marimba-leve` | arpejo de marimba a 92 BPM, sem batida |
| 4 | `4-piano-lofi` | piano elétrico com tremolo, quente |
| 5 | `5-minimal-tech` | pulso grave suave e brilho agudo |

## 1. Escolher os setores

1. Ler `<projeto>/planejamento/registro-videos.md` e achar o ciclo atual.
2. Listar os setores da tabela do `CLAUDE.md` que ainda não saíram nele.
   Vídeo fora da lista (ex.: Lilo) não conta para o ciclo.
3. Escolher 2 setores diferentes, de nichos diferentes quando der. Dê
   preferência ao que já tem pendência em `planejamento/semana-NN.md`.
4. Se faltam menos de 2 setores, fechar o ciclo: anotar "Ciclo N+1" no
   registro e completar com setores do ciclo novo.
5. Mostrar ao usuário os 2 setores, o nicho e a loja de demonstração de
   cada um. Seguir sem esperar resposta, salvo se ele pediu para confirmar.

Loja de demonstração por nicho (semeada só no Supabase local):

| Nicho | Loja | Semente |
|---|---|---|
| CG, AT | Aurora Celulares | `semear-video.sql` da `/brag-instagram` |
| BAR | barbearia fictícia | `semear-barbearia.sql` da `/brag-instagram` |
| CLI, PS | não existe ainda | parar e pedir ao usuário antes de criar uma semente nova |

## 2. Roteiro

Para cada setor, escrever `<projeto>/planejamento/roteiros/<setor>.md` no
formato de `roteiros/lilo.md`: tabela de cenas (tela, fala, segundos),
regras aplicadas e a legenda do post. `<setor>` é uma palavra só, em
minúsculas: `pdv`, `caixa`, `os`, `estoque`, `agenda`…

Conferir cada afirmação do roteiro no código de `C:\dev\Nallon` ou em
`C:\dev\Nallon\docs\ai\reference\modules\`. Se o setor é Pro, a fala e a
legenda dizem "no plano Pro". A última fala é a assinatura do `CLAUDE.md`.

## 3. Gerar cada vídeo

Rodar a `/brag-instagram` dentro de `C:\dev\Nallon`, uma vez por setor, com o
roteiro do passo 2 como plano. Pasta de saída:
`C:\dev\Nallon\brag-output-<data>-<setor>`.

Música (substitui o "Usar `/media-use` para achar a faixa" da
`/brag-instagram`, salvo `--no-music`): depois de medir a duração final do
vídeo, gerar a trilha com essa duração e usar a escolhida.

```bash
python <skill-dir>/trilhas.py assets/music <segundos>
```

Em `assets/music/`, ficar só com `<n>-*.wav` da `--trilha` escolhida e
apontar o `<audio>` da música para ele. O ducking e o volume seguem a
`/brag-instagram`.

Os 2 vídeos são independentes. Terminar e conferir o primeiro (checagem da
`/brag-instagram`) antes de começar o segundo.

## 4. Copiar, registrar e versionar

Para cada vídeo, de `C:\dev\Nallon\brag-output-<data>-<setor>`:

| Origem | Destino em `<projeto>/videos/` |
|---|---|
| `brag.mp4` | `<data>-<setor>.mp4` |
| `brag.jpg` | `<data>-<setor>.jpg` |
| `share-copy.txt` | `<data>-<setor>.txt` |

Acrescentar uma linha por vídeo em `planejamento/registro-videos.md`:
`| <data> | <nome do setor> (<nicho>) | videos/<data>-<setor>.mp4 | não |`.
Se o setor tinha pendência em `semana-NN.md`, riscar a pendência.

Mostrar os vídeos ao usuário com `SendUserFile` (mp4 e capa). Com o ok dele,
fazer o commit em `<projeto>` (`feat(videos): <setor-a> e <setor-b> de <data>`)
e o push. O repositório é público: antes do commit, `git status` não pode
listar `.MOV`, `.DNG`, `.wav` nem nada de `brag-output`.

## Checagem antes de dizer pronto

- Os 2 setores não saíram antes no ciclo e são diferentes entre si.
- Cada vídeo passou na checagem da `/brag-instagram` e termina com a
  assinatura exata do `CLAUDE.md`.
- `videos/` tem `mp4`, `jpg` e `txt` de cada setor, com o nome certo.
- O registro tem uma linha por vídeo novo.
- `git status` em `<projeto>` está limpo depois do push.
