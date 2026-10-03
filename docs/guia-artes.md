# Guia de artes: prompt padrão do Magnific

Vale para carrossel, post único, story e capa avulsa. A capa de cada Reels
já sai do próprio vídeo (`videos/AAAA-MM-DD-<setor>.jpg`). As regras de
conteúdo e a identidade ficam no `CLAUDE.md` da raiz.

## Configuração fixa no Magnific

| Campo | Valor |
|---|---|
| Modelo | `gpt-2` |
| Qualidade | `low` |
| Resolução | `2k` (1536×2048 no 3:4) |
| Quantidade | `1` |
| Referência | `artes/semana-01/seg-carrossel-01.png`, anexada como imagem de referência |
| "AI prompt" | desligado, para o Magnific não reescrever o texto |
| Feed | `3:4` |
| Stories e capa de Reels | `9:16` |

Custo real medido: 30 créditos por arte em `low 1k` com referência de estilo e 45 em `low 2k` com referência (2026-10-03).

O Instagram exibe o feed em 1080 px de largura, e a arte em `1k` tem 768.
Para subir a resolução há dois caminhos, medidos em 2026-10-03:

| Caminho | Resultado | Custo |
|---|---|---|
| Gerar em `2k` | 1536×2048 | o dobro do `1k` (30 créditos sem referência, contra 15) |
| Image Upscaler, modo Precision, 2x, sobre a arte pronta | 1536×2048, sem mudar o desenho | 90 créditos por arte |

Arte nova que vai para o feed: gere direto em `2k`. O upscaler só compensa
para salvar uma arte já aprovada que não pode mudar.

A geração pode ser feita no site (`magnific.com/app/ai-image-generator`)
ou pelo conector do Magnific, com `images_generate` (modo `gpt-2`, mesma
configuração) e a referência enviada antes como creation, tipo `style`.

## Regra de custo

1. Gere sempre 1 imagem só, começando em `low 2k`.
2. Gere de novo só se o texto sair errado.
3. Se errar, tente mais 1 vez em `low 2k`.
4. Se errar de novo, suba para `medium 2k`.

## Como montar o prompt

1. Escolha o tipo de peça.
2. Copie o bloco de estilo fixo.
3. Cole embaixo o bloco da peça.
4. Troque os textos entre `[ ]`.

Numeração do carrossel: o slide 2 é o sinal "1". Na capa, o número grande é o total de sinais.
Salve as artes em `artes/semana-NN/` com o nome `dia-peça-slide.png`. Exemplo: `artes/semana-01/seg-carrossel-02.png`.

---

## Bloco de estilo fixo (não mude)

```
Flat editorial Instagram graphic. Warm cream background #f5f1ea. Near-black text #1a1714. Single accent color amber #e8a33d, used only for numbers, pills and small highlights. Bold geometric sans-serif headlines, left-aligned, with generous margins and lots of whitespace. Body text in a clean regular sans-serif. Thin near-black line-art illustrations with flat amber fills. No gradients, no shadows, no photos, no 3D. Footer with small bold wordmark "Nallon" at bottom left. All text in Brazilian Portuguese with correct accents, rendered exactly as written. No extra text beyond what is specified.
```

## Blocos por tipo de peça

**1. Capa de carrossel**
```
Cover slide. Huge amber number "[N]" at top left, next to a large headline: "[TÍTULO]". Below, an amber rounded pill with the text "[SUBTÍTULO]". Lower right: line-art illustration of [CENA]. Bottom right small text "arraste →".
```

**2. Slide interno de carrossel**
```
Interior slide [N] of a carousel. Top left, amber circle with the number "[N]". Headline, large, left-aligned: "[FRASE PRINCIPAL]". Below, smaller body text: "[FRASE DE APOIO]". Bottom third: small line-art illustration of [CENA]. Bottom right small text "arraste →".
```

**3. Slide final (CTA)**
```
Closing slide. Large headline: "[PERGUNTA OU CHAMADA]". Below, an amber rounded pill: "[AÇÃO]". Small line-art icon of [ÍCONE]. No "arraste" text.
```

**4. Post único**
```
Single post. Large headline: "[TÍTULO]". Smaller line below: "[APOIO]". Right half: line-art illustration of [CENA]. Bottom right small amber pill: "[CTA CURTO]".
```

**5. Story**
```
Vertical Instagram story layout. Headline centered in the upper third: "[TEXTO]". Leave the middle third empty for an Instagram sticker (poll, question or link). Small line-art illustration of [CENA] in the bottom third.
```
