---
name: reels-nallon
description: Produz os Reels do dia do Nallon de ponta a ponta. Escolhe 2 setores pelo ciclo do registro, gera cada vídeo com a /brag-instagram e a trilha ambiente própria, copia para videos/, registra, faz o commit e sobe o mp4 para o Release do mês. Use quando o usuário disser "/reels-nallon", "vídeos do dia", "faz os reels de hoje" ou "próximos vídeos do Nallon".
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
| `--trilha <1-5>` | `1` (`aurora`) |
| `--data AAAA-MM-DD` | hoje |
| `--voz`, `--sem-voz`, `--no-music`, `--no-sfx` | repassadas à `/brag-instagram` |

Trilhas, geradas por `<skill-dir>/trilhas.py`:

| # | Arquivo | Clima |
|---|---|---|
| 1 | `1-aurora` | pad quente em tom maior com notas esparsas de piano elétrico; calmo e confiante |
| 2 | `2-vidro` | acordes de piano elétrico a 76 BPM; quente, produto bem-acabado |
| 3 | `3-pulso` | arpejo com eco e pulso grave macio a 100 BPM; movimento, tecnologia |
| 4 | `4-manha` | piano de feltro a 66 BPM; acolhedor, loja de bairro |
| 5 | `5-horizonte` | crescendo a 90 BPM que sobe até a assinatura |

Nenhuma tem bateria. Todas trocam para o acorde final (tônica) nos últimos
4,5 s ou pouco mais, onde cai a assinatura, e saem em fade de 2 s. Para
ouvir antes de escolher: `python <skill-dir>/trilhas.py <projeto>/amostras-som`
(pasta fora do git).

## 1. Escolher os setores

1. Ler `<projeto>/planejamento/registro-videos.md` e achar o ciclo atual.
2. Listar os setores da tabela do `CLAUDE.md` que ainda não saíram nele.
   Linha "extra" não conta para o ciclo. Vídeo extra só a pedido do
   usuário; segue os passos 2 a 4 com o tema no lugar do setor.
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

Para cada setor, escrever `<projeto>/planejamento/roteiros/<setor>.md`.
`<setor>` é uma palavra só, em minúsculas: `pdv`, `caixa`, `os`, `estoque`,
`agenda`… Formato:

```markdown
# Reels: <nome do setor>

Setor: <setor>. Nicho: <sigla>. Voz: `narrador`. Trilha: <n> (<nome>).
Duração alvo: <n> s. Loja fictícia "<loja>", só no app local.

| # | Tela (app local) | Fala | ~s |
|---|---|---|---|
| 1 | <o que aparece> | <fala da cena> | 2,5 |
| … | | | |
| n | Encerramento limpo: logo do Nallon e assinatura | Nallon. Gestão inteligente para o seu negócio. | 4 |

Regras aplicadas: <quais regras do CLAUDE.md pesaram neste roteiro>.

## Legenda do post

<texto do `share-copy.txt`>
```

Conferir cada afirmação do roteiro no código de `C:\dev\Nallon` ou em
`C:\dev\Nallon\docs\ai\reference\modules\`. Se o setor é Pro, a fala e a
legenda dizem "no plano Pro". A última fala é a assinatura do `CLAUDE.md`.

## 3. Gerar cada vídeo

Antes de compor, ler `<projeto>/docs/direcao-visual-reels.md`: formato
exigido pelo Instagram, zona segura, legenda, movimento e encerramento.

Rodar a `/brag-instagram` dentro de `C:\dev\Nallon`, uma vez por setor, com o
roteiro do passo 2 como plano. Pasta de saída:
`C:\dev\Nallon\brag-output-<data>-<setor>`.

Música (substitui o "Usar `/media-use` para achar a faixa" da
`/brag-instagram`, salvo `--no-music`): depois de medir a duração final do
vídeo, gerar a trilha com essa duração e usar a escolhida.

```bash
python <skill-dir>/trilhas.py assets/music <segundos> <n>
```

Sai só `assets/music/<n>-<nome>.wav`, da `--trilha` escolhida. Apontar o
`<audio>` da música para ele. O ducking e o volume seguem a
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

Acrescentar uma linha por vídeo em `planejamento/registro-videos.md`, com
as duas últimas colunas vazias até o post sair:
`| <data> | <nome do setor> | <nicho> | <data>-<setor> | | |`.
Se o setor tinha pendência em `semana-NN.md`, riscar a pendência.

Mostrar os vídeos ao usuário com `SendUserFile` (mp4 e capa). Com o ok dele,
de dentro de `<projeto>`:

1. Commit (`feat(videos): <setor-a> e <setor-b> de <data>`) e push. Entram
   só a capa, a legenda, o roteiro e o registro. O repositório é público:
   o `.gitignore` já barra `.mp4`, áudio e material bruto; não forçar
   nenhum deles com `git add -f`.
2. Subir cada `.mp4` para o Release do mês:

   ```bash
   gh release view reels-<AAAA-MM> >/dev/null 2>&1 || gh release create reels-<AAAA-MM> \
     --title "Reels <AAAA-MM>" --notes "Reels finais do mês. Capa e legenda de cada um ficam em videos/."
   gh release upload reels-<AAAA-MM> videos/<data>-<setor>.mp4 --clobber
   ```

## 5. Publicar (quem publica é o usuário)

Passar esta lista junto com os vídeos:

1. No app: Perfil, Menu, "Seu app e suas mídias", "Qualidade da mídia",
   ligar "Carregar em alta qualidade". Basta uma vez por aparelho.
2. No envio, escolher `<data>-<setor>.jpg` como capa e ajustar o recorte
   da grade. O Instagram não deixa trocar a capa depois de publicar.
3. Colar a legenda do `.txt`. No máximo 5 hashtags: o Instagram ignora as
   que passarem disso.
4. Depois de publicar, preencher "Publicado em" e "Link do post" na linha
   do vídeo em `planejamento/registro-videos.md`.

## Checagem antes de dizer pronto

- Os 2 setores não saíram antes no ciclo e são diferentes entre si.
- Cada vídeo segue `<projeto>/docs/direcao-visual-reels.md` e passa na revisão da seção 10 dela.
- Cada vídeo passou na checagem da `/brag-instagram` (formato, volume, zona
  segura, capa, loop) e termina com a assinatura exata do `CLAUDE.md`.
- Em cada still, título, legenda e o ponto demonstrado da interface estão
  em x 65–1015, y 270–1250.
- A legenda do post tem primeira linha de até 125 caracteres, "link na
  bio" e de 3 a 5 hashtags, com `#nallon`.
- `videos/` tem `mp4`, `jpg` e `txt` de cada setor, com o nome certo, e o `mp4` está no Release do mês.
- O registro tem uma linha por vídeo novo.
- `git status` em `<projeto>` está limpo depois do push.