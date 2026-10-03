---
name: brag-instagram
description: Gera um Reels do Instagram (1080x1920) do projeto atual com narração em pt-BR, legenda na tela sincronizada com a fala e legenda de post pronta. Usa a skill /brag por baixo. Use quando o usuário disser "/brag-instagram", "vídeo para o Instagram", "faz um reels", "vídeo do site para postar no Instagram" ou "vídeo narrado em português".
---

# /brag-instagram

Roda a skill `/brag` completa com as regras abaixo por cima. Onde este arquivo
contradiz a `/brag`, vale este arquivo.

A `/brag` fica em `~/.claude/skills/brag/` (instalada via `npx skills`; não
editar lá, a atualização sobrescreve).

## Opções

| Opção | Padrão |
|---|---|
| `--voz <perfil>\|pf_dora\|pm_alex` | `narrador`: voz masculina sintética, OmniVoice (perfil em `~/.hyperframes/vozes/<perfil>/`). `pf_dora` (feminina) e `pm_alex` (masculina) usam o Kokoro |
| `--sem-voz` | narração ligada |
| `--tone`, `--duration`, `--no-music`, `--no-sfx`, `--title` | repassadas à `/brag` |

## Como rodar

1. Ler `~/.claude/skills/brag/SKILL.md` e seguir o fluxo completo dela.
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

No Nallon há uma loja fictícia por nicho. Cada `.sql` fica nesta pasta, é
idempotente e roda só no Supabase local:

| Nicho | Loja | Arquivo | Login em `localhost:3000/entrar` |
|---|---|---|---|
| CG, AT | Aurora Celulares (7 produtos, 4 serviços, 7 clientes, 7 OS) | `semear-video.sql` | `carlos@video.local` |
| BAR | Barbearia Ponto Certo (4 serviços, 3 profissionais, agenda de hoje e amanhã) | `semear-barbearia.sql` | `diego@video.local` |
| CLI | Clínica Vida Plena (consultas, 3 profissionais, agenda de hoje e amanhã) | `semear-clinica.sql` | `helena@video.local` |
| PS | Ar Frio Climatização (4 serviços, 3 técnicos, agenda de hoje e amanhã) | `semear-servicos.sql` | `andre@video.local` |

```bash
docker exec -i supabase_db_nallon psql -U postgres -d postgres < ~/.claude/skills/brag-instagram/semear-video.sql
```

A senha de cada login está no cabeçalho do `.sql`. As três lojas com
agenda têm página pública em `/agendar/<slug>` (o slug também está no
cabeçalho). O banco local é zerado de vez em quando: se o login falhar,
rodar o `.sql` de novo.

Os quatro logins são administradores da própria loja. O caixa nasce
fechado: abrir o caixa antes de gravar uma venda. Venda e caixa aberto ficam
no banco depois do vídeo; o `.sql` não desfaz isso.

Subir o app de dentro de `C:\dev\Nallon` (`npm run dev`, em segundo plano):
o `preview_start` só acha o `launch.json` quando a sessão nasceu lá. Antes
de capturar, conferir que o login funciona. Se der "Não conseguimos falar
com o servidor", o `.env.development.local` aponta para uma porta sem
Supabase: subir o app com `NEXT_PUBLIC_SUPABASE_URL` e
`NEXT_PUBLIC_SUPABASE_ANON_KEY` na linha de comando, com os valores de
`supabase status -o json`, sem editar nenhum `.env`. O `.env.local` aponta
para produção: nunca usar nem copiar.

Não usar o modo demonstração: localmente faltam
`DEMO_LOJA_ID` e `DEMO_SENHA`. Erro de coluna ou constraint no `.sql`: o
schema mudou; ajustar o `.sql` pelas migrations e testar trocando o nome
da loja e o `commit` por `rollback` numa cópia.

## Direção visual (passos 2 e 3)

Antes do plano, ler `C:\dev\Insta Nallon\docs\direcao-visual-reels.md`
inteiro. É a fonte única de formato, zona segura, capa, fundo, interface,
moldura, composição, texto na tela, legenda, movimento e encerramento. Este
arquivo não repete essas regras: traz só o que é de execução.

- **Duração.** 20 a 30 s. Vale este número, não os 15 a 25 s da `/brag`.
- **Layout de referência.** Título em y 282–368; painel da interface de y 430 a y 1240; legenda abaixo do painel, entre y 1280 e y 1500. A legenda nunca fica em cima da interface.
- **Fontes e logo.** O `lint` exige `@font-face` local. Space Grotesk 700 e Geist estão em `C:\dev\Nallon\brag-output-2026-10-03-pdv\composition\assets\`, junto com a logo; copiar de lá.
- **Passos da `/brag` que não se aplicam:** áudio-reativo, beat sync, espera de aprovação no `preview`, pôster tirado do render e `share-copy` de 1 a 3 frases.
- **UI em pé.** Não encolher tela de desktop. Capturar o app em viewport de celular (390px de largura, escala 3) ou aproximar a câmera em uma coluna, um card ou um formulário por vez.
- **Loop.** O Reels repete sozinho. O último frame emenda no primeiro sem salto: mesmo fundo e mesma cor base do gancho, sem fade para preto. A música não termina em silêncio longo; sai junto com o último frame. A última fala fecha a ideia.

A assinatura falada que encerra todo vídeo está em
`C:\dev\Insta Nallon\CLAUDE.md`, seção "Encerramento obrigatório de todo
vídeo". Nenhuma fala depois dela.

## Narração (passo 3, substitui a seção "Voiceover" da `/brag`)

### Roteiro

No `brag-plan.md`, seção `## Roteiro da narração`: uma fala por cena.

- Descrever o que acontece na tela, em frases curtas e naturais: "A busca
  acha o cabo. O Pix fecha a venda." Não ler o texto que já está escrito.
- 2,2 a 2,6 palavras por segundo de cena. Cena de 4s: no máximo 10 palavras.
- Escrever para o ouvido, não para o olho: moeda e siglas lidas como
  palavra por extenso. Erros confirmados no Kokoro: "R$" sai "reais
  dólar" e a vírgula do valor é lida "vírgula" (para "R$ 47,00", escrever
  "quarenta e sete reais"); "OS" sai "ôs" (escrever "ó ésse").
- Com Kokoro, conferir como a voz lê nomes, siglas e números do roteiro
  antes de gerar:

  ```bash
  PYTHONIOENCODING=utf-8 ~/.hyperframes/tts-venv/Scripts/python.exe -c \
    "from kokoro_onnx.tokenizer import Tokenizer; t=Tokenizer(); \
     [print(s, '->', t.phonemize(s, lang='pt-br')) for s in ['OS', 'PDV']]"
  ```

  Fonema estranho: reescrever como se fala e conferir de novo.
- A legenda na tela usa a grafia normal ("R$ 47,00"), não a falada.

### Gerar a fala: OmniVoice (padrão)

Instalado global com `uv tool install omnivoice` (Python 3.12, torch
cu128). Se `omnivoice-infer-batch` não estiver no PATH, instalar:

```bash
uv tool install omnivoice --python 3.12 --torch-backend cu128 --with "torch==2.8.0" --with "torchaudio==2.8.0"
```

O perfil `~/.hyperframes/vozes/<perfil>/` guarda `ref.wav` (3 a 10s de
fala em pt-BR) e `ref.txt` (o texto exato dito no `ref.wav`). Toda cena
clona o `ref.wav`, então a voz fica igual do começo ao fim.

O perfil padrão `narrador` é uma voz masculina sintética, grave e calma,
criada por descrição; o `ref.wav` é uma amostra de 8,3s dela (o ref.txt
traz números por extenso). Seguem disponíveis `--voz minha-voz` (voz do
usuário, clonada de um trecho de 6,5s de `Downloads/minah voz.mp3`) e
`--voz narradora` (sintética feminina, jovem, limpa e suave). A
`narradora` foi criada uma vez por descrição
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
  ~/.claude/skills/brag-instagram/conferir-fala.py assets/vo-*.wav
```

Fala que não bate com o roteiro: regerar só aquela linha (jsonl com uma
linha). O Whisper escreve número e sigla na grafia normal ("R$ 47,00"),
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
- Música em volume 0,14 fixo quando a fala é quase contínua. Só sobe
  (até 0,35) em trecho de mais de 2 s sem fala.

### Legenda na tela

Aparência, tamanho e posição: seção 7 da direção visual. Na execução:

- A legenda nunca fica em cima da interface, de moldura ou de outro texto. Fica na faixa própria, abaixo do painel.
- A frase da cena aparece enquanto é falada: entra com a fala e sai com ela.
- Calcular o contraste do par de cores no plano, antes de compor (o `hyperframes check` exige 4,5:1). O destaque em âmbar também passa por essa conta contra o fundo da caixa.
- A caixa da legenda não se sobrepõe a outro texto da cena (`content_overlap` no `check`): reservar o lugar dela no storyboard.

#### Palavra por palavra (destaque da palavra falada)

A frase inteira fica na tela; a palavra sendo falada ganha destaque
(cor da marca ou peso maior). Precisa do tempo de cada palavra, que nem
o OmniVoice nem o Kokoro dão. O `conferir-fala.py` (em "Gerar a fala")
já grava `assets/vo-NN.json` ao lado de cada WAV, com o tempo de cada
palavra dito pelo Whisper, no formato de transcrição das legendas
(`[{"id": "w0", "text": "O", "start": 0.0, "end": 0.3}, ...]`). Com
Kokoro, rodar o mesmo script nos WAVs dele.

- O Whisper escreve na grafia normal, mas quebra número e moeda em
  pedaços: "R$ 47,00" vira `R`, `$`, `47`, `,00`. A legenda mostra a
  palavra do roteiro: alinhar pela ordem, e uma palavra do roteiro que
  corresponde a vários pedaços destaca do início do primeiro ao fim do
  último.
- Montagem da legenda: `~/.claude/skills/media-use/audio/references/captions/authoring.md`.
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

`brag.jpg` em 1080x1920, montada no modelo fixo da seção "Capa" da direção
visual (pílula do setor, título, painel da interface e marca, sempre nos
mesmos lugares). É um HTML separado (`capa.html`), fotografado em
1080x1920, fora da composição: não vira cena do vídeo. Gravada como frame 0
do `brag.mp4`, é a única exceção à regra "logo só no encerramento".

### Volume

Depois de gravar a capa como frame 0, normalizar para o Instagram
(vídeo copiado, frame 0 preservado). De `<output-dir>`:

```bash
ffmpeg -y -i brag.mp4 -c:v copy -af loudnorm=I=-14:TP=-1.5:LRA=11 \
  -ar 48000 -c:a aac -b:a 192k -movflags +faststart brag.norm.mp4 \
  && mv brag.norm.mp4 brag.mp4
```

### Legenda do post

`share-copy.txt` no formato do Instagram, em pt-BR:

1. Primeira linha com até 125 caracteres: é o que aparece antes do "mais".
   Diz o que o produto faz e para quem.
2. Uma ou duas linhas de apoio, com a copy real do site.
3. "Link na bio." URL escrita não vira link na legenda do Instagram.
4. De 3 a 5 hashtags específicas do nicho, em pt-BR. Nunca mais de 5: o
   Instagram ignora as que passarem disso.

## Checagem antes de dizer pronto

- Formato (`ffprobe -v error -show_streams brag.mp4`): 1080x1920, 30 fps
  constantes, H.264 `yuv420p` progressivo, AAC estéreo 48 kHz a 128 kbps ou
  mais. Duração de 20 a 30 s.
- Volume: `ffmpeg -i brag.mp4 -af loudnorm=print_format=summary -f null -`
  dá cerca de -14 LUFS e pico ≤ -1 dBTP.
- Zona segura: gerar a folha de conferência e olhar com Read. O retângulo
  vermelho (x 65–1015, y 270–1240) contém título, logo e o painel inteiro.
  O retângulo amarelo (y 1280–1500) contém a legenda. Fora dos dois, só
  fundo.

  ```bash
  ffmpeg -y -v error -i brag.mp4 -vf "fps=1/2,drawbox=65:270:950:970:red:4,drawbox=65:1280:950:220:yellow:4,scale=360:-1,tile=5x3" -frames:v 1 zona-segura.jpg
  ```

  Sai um quadro a cada 2 s, até 15 (30 s de vídeo). Quadro que cair em
  transição mostra duas telas sobrepostas: é esperado.
- Legenda fora da interface: em nenhum quadro a caixa da legenda encosta
  no painel. Se encostar, o vídeo não está pronto.
- Stills de cada cena: legenda sincronizada com a fala, nada cortado,
  quadro cheio e sem barras pretas.
- `brag.jpg` segue o modelo fixo de capa e é legível no recorte 3:4 central.
- Loop: o último quadro e o frame 1 (o primeiro depois da capa), lado a
  lado, não mostram salto de fundo ou cor.

  ```bash
  ffmpeg -y -v error -sseof -0.04 -i brag.mp4 -frames:v 1 fim.png
  ffmpeg -y -v error -i brag.mp4 -vf "select=eq(n\,1)" -frames:v 1 inicio.png
  ffmpeg -y -v error -i fim.png -i inicio.png -filter_complex hstack loop.jpg
  ```
- `git status` no repositório não lista nada de `brag-output`.
