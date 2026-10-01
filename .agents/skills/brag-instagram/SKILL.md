---
name: brag-instagram
description: Gera um Reels do Instagram (1080x1920) do projeto atual com narração em pt-BR, legenda na tela sincronizada com a fala e legenda de post pronta. Usa a skill /brag por baixo. Use quando o usuário disser "/brag-instagram", "vídeo para o Instagram", "faz um reels", "vídeo do site para postar no Instagram" ou "vídeo narrado em português".
---

# /brag-instagram

Roda a skill `/brag` completa com as regras abaixo por cima. Onde este arquivo
contradiz a `/brag`, vale este arquivo.

A `/brag` fica em `~/.Codex/skills/brag/` (instalada via `npx skills`; não
editar lá, a atualização sobrescreve).

## Opções

| Opção | Padrão |
|---|---|
| `--voz <perfil>\|pf_dora\|pm_alex` | `minha-voz`: voz do usuário clonada, OmniVoice (perfil em `~/.hyperframes/vozes/<perfil>/`). `pf_dora` (feminina) e `pm_alex` (masculina) usam o Kokoro |
| `--sem-voz` | narração ligada |
| `--tone`, `--duration`, `--no-music`, `--no-sfx`, `--title` | repassadas à `/brag` |

## Como rodar

1. Ler `~/.Codex/skills/brag/SKILL.md` e seguir o fluxo completo dela.
   Pular o "Model check": o `slim.md` não tem narração. Formato fixo
   `vertical` (1080x1920, 30fps). Narração ligada, salvo `--sem-voz`.
2. Aplicar as seções abaixo nos passos 2 (plano), 3 (composição) e 4
   (entrega) da `/brag`.

## Pasta de saída fora do git

Antes de gravar qualquer arquivo, de dentro do repositório:

```bash
f="$(git rev-parse --git-common-dir)/info/exclude"; grep -qxF 'brag-output*/' "$f" || echo 'brag-output*/' >> "$f"
```

(`git check-ignore brag-output` falha enquanto a pasta não existe, porque
o padrão com `/` só casa diretório: não usar como teste.)

`info/exclude` vale só nesta máquina: sem commit, sem PR. Vídeo, PNG e WAV
nunca entram no repositório.

## Dados na tela

O vídeo é público. Capturar só do app rodando localmente (`localhost`), com
dados fictícios semeados para o vídeo: loja, clientes, telefones, valores.
Nunca capturar de produção nem de sessão logada com dados reais. Antes de
renderizar, olhar cada still procurando nome, telefone, e-mail ou valor
que pareça real.

No Nallon, a loja fictícia "Aurora Celulares" (7 produtos, 4 serviços,
7 clientes, 7 OS em status variados) vem de
`~/.Codex/skills/brag-instagram/semear-video.sql`. Idempotente; roda só
no Supabase local:

```bash
docker exec -i supabase_db_sistema-connect psql -U postgres -d postgres < ~/.Codex/skills/brag-instagram/semear-video.sql
```

Rodando de um worktree sem `.env*`: copiar só o `.env.development.local`
do checkout principal (aponta para `127.0.0.1:54321`). O `.env.local` de
lá aponta para produção: nunca copiar. Subir o app com `preview_start`
(`connect`), depois de `npm ci`.

Login em `localhost:3000/entrar`: `carlos@video.local`, senha no
cabeçalho do `.sql`. Não usar o modo demonstração: localmente faltam
`DEMO_LOJA_ID` e `DEMO_SENHA`. Erro de coluna ou constraint no `.sql`: o
schema mudou; ajustar o `.sql` pelas migrations e testar trocando o nome
da loja e o `commit` por `rollback` numa cópia.

## Formato Reels (passos 2 e 3)

- **Área segura.** A interface do Instagram cobre o vídeo: 250px no topo,
  420px na base (legenda e perfil), 120px na direita (botões), 60px na
  esquerda. Texto, legenda e UI importante ficam dentro de
  x 60–960, y 250–1500.
- **UI em pé.** Não encolher tela de desktop. Capturar o app em viewport de
  celular (390px de largura, escala 3) ou aproximar a câmera em uma coluna,
  um card ou um formulário por vez.
- **Gancho no primeiro segundo.** Nada de logo abrindo o vídeo. Frame 1 já
  mostra a frase de impacto ou o produto trabalhando. Logo só no fecho.
- **Duração.** 20–30s; a fala define o ritmo.
- **Loop.** O Reels repete sozinho. O último frame precisa emendar no
  primeiro sem salto: mesmo fundo e mesma cor base do gancho, sem fade para
  preto. A música não termina em silêncio longo; corta junto com o último
  frame. A última fala fecha a ideia (não termina em "e...").

## Encerramento obrigatório (projeto Nallon)

Todo vídeo do Nallon termina com a narração exata "Nallon. Gestão inteligente
para o seu negócio." (regra completa no `CLAUDE.md` de `C:\dev\Insta Nallon`).
É a última fala do roteiro: nada depois dela, pausa curta após "Nallon", logo
do Nallon na tela junto, legenda igual à fala. A cena final dura o suficiente
para a frase inteira e a logo assentarem.

## Narração (passo 3, substitui a seção "Voiceover" da `/brag`)

### Roteiro

No `brag-plan.md`, seção `## Roteiro da narração`: uma fala por cena.

- Descrever o que acontece na tela, em frases curtas e naturais: "A busca
  acha o cabo. O Pix fecha a venda." Não ler o texto que já está escrito.
- 2,2 a 2,6 palavras por segundo de cena. Cena de 4s: no máximo 10 palavras.
- Escrever para o ouvido, não para o olho: moeda e siglas lidas como
  palavra por extenso. Erros confirmados no Kokoro: "R$ 39,90" sai
  "reais dólar trinta e nove vírgula noventa" (escrever "trinta e nove e
  noventa"); "OS" sai "ôs" (escrever "ó ésse").
- Com Kokoro, conferir como a voz lê nomes, siglas e números do roteiro
  antes de gerar:

  ```bash
  PYTHONIOENCODING=utf-8 ~/.hyperframes/tts-venv/Scripts/python.exe -c \
    "from kokoro_onnx.tokenizer import Tokenizer; t=Tokenizer(); \
     [print(s, '->', t.phonemize(s, lang='pt-br')) for s in ['OS', 'PDV']]"
  ```

  Fonema estranho: reescrever como se fala e conferir de novo.
- A legenda na tela usa a grafia normal ("R$ 39,90"), não a falada.

### Gerar a fala: OmniVoice (padrão)

Instalado global com `uv tool install omnivoice` (Python 3.12, torch
cu128). Se `omnivoice-infer-batch` não estiver no PATH, instalar:

```bash
uv tool install omnivoice --python 3.12 --torch-backend cu128 --with "torch==2.8.0" --with "torchaudio==2.8.0"
```

O perfil `~/.hyperframes/vozes/<perfil>/` guarda `ref.wav` (3 a 10s de
fala em pt-BR) e `ref.txt` (o texto exato dito no `ref.wav`). Toda cena
clona o `ref.wav`, então a voz fica igual do começo ao fim.

O perfil padrão `minha-voz` é a voz do usuário, clonada de um trecho de
6,5s de `Downloads/minah voz.mp3` (o ref.txt traz números por extenso). O
perfil `narradora` (sintética feminina, jovem, limpa e suave) segue
disponível com `--voz narradora`. Ela foi criada uma vez por descrição
(`"instruct": "female, young adult, moderate pitch"`, sem `ref_audio`) e
o áudio gerado virou o `ref.wav`. Não usar `instruct` direto nas cenas:
cada geração sai com uma voz diferente. Perfil ausente: gerar com Kokoro
`pf_dora` (abaixo) e dizer isso na entrega.

Todas as cenas numa chamada só (o modelo carrega uma vez). De dentro de
`<output-dir>/composition/`, escrever `assets/vo.jsonl` com uma linha por
cena, `ref_audio` em caminho absoluto:

```json
{"id": "vo-01", "text": "<fala da cena>", "ref_audio": "C:/Users/Mau/.hyperframes/vozes/<perfil>/ref.wav", "ref_text": "<conteúdo de ref.txt>", "language_id": "pt"}
```

```bash
PYTHONWARNINGS=ignore omnivoice-infer-batch --model k2-fsa/OmniVoice \
  --test_list assets/vo.jsonl --res_dir assets
```

Sai `assets/vo-01.wav`, `assets/vo-02.wav`... O modelo é de difusão e às
vezes troca ou engole palavra. Conferir cada fala transcrevendo com o
Whisper (já em cache):

```bash
PYTHONIOENCODING=utf-8 "$(uv tool dir)/omnivoice/Scripts/python.exe" \
  ~/.Codex/skills/brag-instagram/conferir-fala.py assets/vo-*.wav
```

Fala que não bate com o roteiro: regerar só aquela linha (jsonl com uma
linha). O Whisper escreve número e sigla na grafia normal ("R$ 39,90"),
então a checagem não pega pronúncia errada de número: escrever para o
ouvido vale aqui também.

### Gerar a fala: Kokoro (`--voz pf_dora|pm_alex`)

Um arquivo por cena, de dentro de `<output-dir>/composition/`:

```bash
HYPERFRAMES_PYTHON="$HOME/.hyperframes/tts-venv/Scripts/python.exe" \
  npx hyperframes tts "<fala da cena>" --voice pf_dora --lang pt-br \
  --output assets/vo-01.wav
```

Se `~/.hyperframes/tts-venv` não existir, criar antes:

```bash
uv venv --python 3.12 ~/.hyperframes/tts-venv
uv pip install --python ~/.hyperframes/tts-venv/Scripts/python.exe kokoro-onnx soundfile
```

### Duração das cenas

Medir cada arquivo (`ffprobe -v error -show_entries format=duration -of csv=p=0 assets/vo-01.wav`).
Duração da cena = duração da fala + 0,4 a 0,8s de respiro. Refazer o
storyboard com esses valores antes de compor.

### Montar

- Cada `vo-NN.wav` em `<audio>` próprio, começando junto com a cena, em
  track-index próprio.
- Todo vídeo leva música ambiente de fundo, do primeiro ao último frame:
  instrumental, suave, sem letra e sem batida forte. Só sem música com
  `--no-music`. Usar `/media-use` para achar a faixa.
- Música abaixa para 0,12–0,15 enquanto há fala e volta depois
  (regra de ducking da `/brag`).

### Legenda na tela

Quem assiste sem som precisa entender o vídeo.

- A frase da cena aparece escrita enquanto é falada: entra com a fala e sai
  com ela.
- Uma a duas linhas, fonte do projeto, peso forte, ≥ 56px, sobre faixa de
  fundo sólido e opaco (nunca texto direto sobre screenshot ou gradiente).
- Contraste: o `hyperframes check` exige WCAG AA, 4,5:1 (3:1 só para
  texto grande). Escolher o par de cores da faixa e do texto no plano e
  calcular a razão antes de compor; mirar ≥ 7:1 para sobrar margem.
  Destaque da palavra falada também passa por essa conta contra a faixa.
  Texto de cena fora da legenda segue a mesma regra.
- A faixa da legenda não se sobrepõe a outro texto da cena
  (`content_overlap` no `check`): reservar a faixa no storyboard e manter
  títulos e UI fora dela.
- Posição fixa em todas as cenas, dentro da área segura, acima de y 1500.
  Não cobrir a parte da UI que a cena está mostrando.

#### Palavra por palavra (destaque da palavra falada)

A frase inteira fica na tela; a palavra sendo falada ganha destaque
(cor da marca ou peso maior). Precisa do tempo de cada palavra, que nem
o OmniVoice nem o Kokoro dão. O `conferir-fala.py` (em "Gerar a fala")
já grava `assets/vo-NN.json` ao lado de cada WAV, com o tempo de cada
palavra dito pelo Whisper, no formato de transcrição das legendas
(`[{"id": "w0", "text": "O", "start": 0.0, "end": 0.3}, ...]`). Com
Kokoro, rodar o mesmo script nos WAVs dele.

- O Whisper escreve na grafia normal, mas quebra número e moeda em
  pedaços: "R$ 39,90" vira `R`, `$`, `39`, `,90`. A legenda mostra a
  palavra do roteiro: alinhar pela ordem, e uma palavra do roteiro que
  corresponde a vários pedaços destaca do início do primeiro ao fim do
  último.
- Montagem da legenda: `~/.Codex/skills/media-use/audio/references/captions/authoring.md`.
- Script falhou (sem GPU, sem modelo): usar o Parakeet do Hyperframes,
  que roda na CPU e cobre português (instalado em 2026-09-29):

  ```bash
  npx hyperframes transcribe assets/vo-01.wav --engine parakeet --language pt --json \
    && mv transcript.json assets/vo-01.json
  ```

  Grava sempre `transcript.json` na pasta atual: renomear a cada cena.
  Mesmo formato do script, mas escreve nome como soa ("Nalon" para
  "Nallon"): alinhar pela ordem, nunca pelo texto. Reinstalar, se
  sumir (~640 MB, pedir ao usuário antes):
  `: > npmrc-vazio && NPM_CONFIG_USERCONFIG="$PWD/npmrc-vazio" npx hyperframes models install parakeet`
  (sem isso, o `allow-scripts=` do `~/.npmrc` dá `EALLOWSCRIPTS`).
- Parakeet também falhou: ficar na legenda por frase acima e dizer isso
  na entrega. Não estimar tempo de palavra por contagem de letras.

## Armadilhas no Windows

Erros que já custaram tempo em execuções anteriores:

- **`hyperframes init`** instala skills sem pedir. Rodar com
  `HYPERFRAMES_SKIP_SKILLS=1` e
  `--non-interactive --resolution portrait --skip-transcribe`.
- **`snapshot --describe`** falha com `EALLOWSCRIPTS` ao instalar
  `@google/genai`. Passar `--describe false` e olhar os stills com Read.
- **Caminho com `C:` em filtro do ffmpeg** (`ametadata=file=`,
  `subtitles=`, `movie=`): o `:` quebra o filtro. Rodar da pasta do arquivo
  e passar caminho relativo.
- **`/tmp` dentro de código** (`python -c "open('/tmp/x')"`, script Node):
  o Git Bash só converte caminho passado como argumento; dentro do código,
  Python e Node leem `C:\tmp`. Usar caminho relativo em `<output-dir>`.
- **`UnicodeEncodeError` (cp1252)** ao imprimir texto em pt-BR de Python:
  prefixar `PYTHONIOENCODING=utf-8`. Vale também para gerar o `vo.jsonl`
  com `print` do Python: sem isso sai em cp1252 e o
  `omnivoice-infer-batch` quebra com `UnicodeDecodeError`.

## Entrega (passo 4, acrescenta à `/brag`)

### Capa

`brag.jpg` em 1080x1920. O conteúdo principal cabe no recorte 3:4 central
(y 240–1680): é o que aparece na grade do perfil.

### Volume

Depois de gravar a capa como frame 0, normalizar para o Instagram
(vídeo copiado, frame 0 preservado). De `<output-dir>`:

```bash
ffmpeg -y -i brag.mp4 -c:v copy -af loudnorm=I=-14:TP=-1:LRA=11 \
  -ar 48000 -c:a aac -b:a 192k -movflags +faststart brag.norm.mp4 \
  && mv brag.norm.mp4 brag.mp4
```

### Legenda do post

`share-copy.txt` no formato do Instagram, em pt-BR:

1. Primeira linha com até 125 caracteres: é o que aparece antes do "mais".
   Diz o que o produto faz e para quem.
2. Uma ou duas linhas de apoio, com a copy real do site.
3. "Link na bio." URL escrita não vira link na legenda do Instagram.
4. De 3 a 5 hashtags específicas do nicho, em pt-BR.

## Checagem antes de dizer pronto

- `ffprobe`: 1080x1920, 30fps, H.264, AAC 48 kHz.
- Volume: `ffmpeg -i brag.mp4 -af loudnorm=print_format=summary -f null -`
  dá cerca de -14 LUFS e pico ≤ -1 dBTP.
- Stills de cada cena: legenda e texto dentro da área segura, legenda
  sincronizada com a fala, nada cortado.
- `brag.jpg` legível no recorte 3:4 central.
- Loop: `ffmpeg -sseof -0.04 -i brag.mp4 -frames:v 1 fim.png` e o frame 1
  lado a lado não mostram salto de fundo ou cor.
- `git status` no repositório não lista nada de `brag-output`.
