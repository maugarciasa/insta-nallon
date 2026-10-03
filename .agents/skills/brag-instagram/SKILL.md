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
| `--voz <perfil>\|pf_dora\|pm_alex` | `narrador`: voz masculina sintética, OmniVoice (perfil em `~/.hyperframes/vozes/<perfil>/`). `pf_dora` (feminina) e `pm_alex` (masculina) usam o Kokoro |
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

## Formato Reels e Direção de Arte SaaS Premium V2 (passos 2 e 3)

No projeto Nallon, siga a direção de arte de `C:\dev\Insta Nallon\docs\direcao-visual-reels.md`; onde o resumo abaixo divergir dela, vale ela. Peça publicitária premium de software SaaS moderno (referência Linear, Apple, Stripe, Notion). Menos elementos, mais espaço, mais precisão e foco na interface.

- **Formato e Quadro:** Vertical 9:16 (1080 × 1920), 30 FPS. Preencher 100% do quadro. PROIBIDO criar barras pretas laterais ou superiores. Respeitar safe areas do Reels (x 60–960, y 250–1500).
- **Interface e Painel Flutuante:** A interface é o protagonista absoluto, 100% nítida e fiel (sem recriar botões, sem inventar dados, sem blur na UI). Reduzir drasticamente a aparência de "celular genérico": preferir a própria interface como um painel flutuante premium com borda ultrafina refinada (ou sem moldura pesada) e sombra natural suave profunda. A moldura jamais chama mais atenção que o software.
- **Fundo Minimalista:** Fundo creme da marca (`#f5f1ea`), iluminação difusa quase imperceptível. O fundo desaparece visualmente para o sistema brilhar.
- **Composição & Hierarquia:** Em cada momento no máximo: 1) uma mensagem principal; 2) a interface demonstrando; 3) um pequeno elemento secundário. Evitar poluição visual de badge + título + subtítulo + legenda gigante simultâneos.
- **Títulos:** Curtos e focados no benefício ("Gestão em um só lugar"), com excelente kerning e espaçamento generoso. A marca Nallon não se repete em todas as cenas.
- **Badges:** Pequenos, discretos, baixa altura e contraste moderado. Nunca competem com o título.
- **Motion Design:** Câmera aproximando lentamente (zoom de 4% a 12%; até 15% no close de uma funcionalidade), reposicionamento sutil, parallax discreto, fade e slide suave (200 a 500 ms). A cada 1,5 a 3 segundos deve ocorrer uma mudança visual sutil (mudança de foco/aproximação). Sem bounce, shake, zoom agressivo ou efeitos chamativos.
- **Gancho no primeiro segundo.** Frame 1 já mostra a mensagem ou o produto trabalhando. Logo só no fecho.
- **Duração.** 20–30s; a fala define o ritmo.
- **Loop.** O Reels repete sozinho: último frame emenda no primeiro sem salto, música corta junto com o último frame.

## Encerramento obrigatório (projeto Nallon)

Todo vídeo termina com a narração exata "Nallon. Gestão inteligente para o seu negócio."
No encerramento, remover gradualmente a interface. Ficam só a logo do Nallon
(ou o nome NALLON) e a frase "Gestão inteligente para o seu negócio.",
centralizadas. A marca entra com animação discreta, de 0,8 a 1,5 s, e a cena
dura até a fala terminar. Sem CTA nem efeitos luminosos. Nenhuma fala depois.

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
  ~/.Codex/skills/brag-instagram/conferir-fala.py assets/vo-*.wav
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
- Música abaixa para 0,12–0,15 enquanto há fala e volta depois
  (regra de ducking da `/brag`).

### Legenda Editorial Premium (V2)

Quem assiste sem som precisa entender o vídeo. Proibido criar caixas pretas grandes ocupando a largura inferior.

- **Formato compacto editorial:** ocupar entre 55% e 70% da largura do vídeo (max 680-720px), altura mínima necessária, padding equilibrado e cantos arredondados discretos (18-22px). Fundo escuro levemente translúcido (`rgba(22,19,16,0.86)` com `backdrop-filter: blur(14px)`) com sombra muito suave.
- **Frases curtas:** evitar frases longas de 2 ou 3 linhas quando uma frase enxuta transmite a ideia (ex: "Ainda usa vários sistemas?").
- **Destaque exclusivo:** destacar no máximo UMA expressão importante por frase (em tom âmbar #e8a33d). Não usar múltiplas cores simultâneas.
- Contraste: cumpre WCAG AA (≥ 4,5:1).
- Posição fixa dentro da área segura (acima de y 1500).

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