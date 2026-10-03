# Direção visual dos Reels

Vale para todo Reels do Nallon. As regras de conteúdo, a assinatura e a
identidade ficam no `CLAUDE.md` da raiz.

O vídeo é uma peça publicitária de software SaaS moderno, no padrão de
Linear, Apple, Stripe e Notion. A interface real do Nallon é a protagonista.
Menos elementos, mais espaço, mais precisão.

Não pode parecer: template pronto, Canva, apresentação de slides, vídeo
automático de IA, propaganda genérica de aplicativo ou mockup exagerado.

## 1. Formato

- Vertical 9:16, 1080 × 1920, 30 fps constantes.
- Arquivo MP4: vídeo H.264 progressivo, áudio AAC estéreo 48 kHz a 128 kbps ou mais.
- O vídeo preenche 100% do quadro. Sem barras pretas e sem vídeo vertical dentro de outro canvas.
- Duração de 20 a 30 s. A fala define o ritmo.
- O primeiro quadro já mostra a mensagem ou o produto funcionando. Logo só no encerramento.

O Instagram aceita de 1,91:1 a 9:16, exige no mínimo 30 fps e 720 px, e
deixa de recomendar a novos públicos o Reels com mais de 3 minutos.

### Zona segura

O app cobre o vídeo com o nome do perfil, a legenda do post e os botões.
As margens abaixo são as do guia de anúncios da Meta (14% no topo, 35% na
base, 6% de cada lado). A Meta não publica margem para Reels orgânico, e a
do anúncio é a mais exigente: seguindo essa, o vídeo serve nos dois casos e
pode ser turbinado sem refazer.

| Faixa do quadro | O que pode ficar |
|---|---|
| x 65–1015, y 270–1240 | Título, logo, badge e o painel da interface, inteiro |
| x 65–1015, y 1280–1500 | Legenda, sozinha sobre o fundo |
| y 0–270 e y 1500–1920 | Só fundo |

A legenda nunca fica em cima da interface, nem de moldura de celular, nem
de outro texto. O painel termina em y 1240 ou acima; a legenda fica abaixo
dele, com pelo menos 40 px de respiro.

A faixa da legenda fica abaixo da margem de anúncio (y 1250). No Reels
orgânico ela aparece inteira. Se o vídeo for turbinado, a legenda do post
pode cobrir parte dela: nesse caso, exporte uma versão com a legenda na
tela desligada.

Abaixo de y 1000, nada importante à direita de x 960: ali fica a coluna de
botões (curtir, comentar, enviar). Esse recuo é prática do projeto, não
número oficial.

### Capa

- 1080 × 1920, com o conteúdo principal no recorte 3:4 central (y 240–1680), que é o que a grade do perfil mostra.
- A capa é escolhida no envio. O Instagram não deixa trocar depois de publicar.

Toda capa usa o mesmo modelo, para a grade do perfil ficar uniforme. Só
mudam o setor, o título e a tela.

| Elemento | Posição e estilo |
|---|---|
| Fundo | Creme `#f5f1ea`, liso |
| Pílula do setor | Canto em x 90, y 330. Fundo âmbar `#e8a33d`, texto `#1a1714`, Geist semibold 34 px, caixa alta (ex.: "PDV") |
| Título | x 90, topo em y 420, largura até 900 px. Space Grotesk bold 104 px, `#1a1714`, no máximo 2 linhas e 5 palavras. Diz o benefício, sem a marca |
| Painel da interface | Centralizado, 900 px de largura, de y 760 a y 1480. Tela real do setor, com borda ultrafina, cantos de 28 px e a sombra do vídeo |
| Marca | "Nallon" em Space Grotesk bold 44 px, `#1a1714`, x 90, base em y 1600 |

Nada além desses cinco elementos: sem legenda, badge, preço ou seta.

## 2. Fundo

- Creme da marca, `#f5f1ea`.
- Só luz difusa, gradiente quase imperceptível e profundidade discreta.
- Sem elemento decorativo. O fundo some e deixa o sistema aparecer.

## 3. Interface

A interface do Nallon fica fiel à real. Não recrie botões, não mude textos,
números ou layout, não redesenhe componentes e não invente informação.

- Nitidez máxima: todo texto do sistema continua legível.
- Sem blur forte sobre a interface principal.

## 4. Moldura

- Prefira a própria interface como painel flutuante: borda ultrafina, cantos arredondados e sombra natural, suave e profunda.
- Moldura de celular só quando ajudar, e então: fina, com proporção correta, sem borda preta grossa.
- A moldura nunca chama mais atenção que o software.

## 5. Composição

Em cada momento, no máximo:

1. uma mensagem principal;
2. a interface demonstrando essa mensagem;
3. um elemento secundário pequeno.

Não mostre ao mesmo tempo badge grande, título grande, subtítulo, legenda
enorme, CTA e interface completa.

## 6. Texto na tela

**Títulos.** Curtos e sobre o benefício: "Gestão em um só lugar", não
"Nallon Gestão Integrada". A marca não se repete em todas as cenas.
Space Grotesk semibold ou bold, kerning cuidado, alinhamento preciso e
bastante espaço vertical. O título nunca encosta no painel.

**Badges** (ex.: "PRO"). Pequenos, baixos, com contraste moderado. Nunca
competem com o título.

**Tipografia.** Títulos em Space Grotesk, texto em Geist. Pesos medium,
semibold e bold; texto secundário mais leve. No máximo três níveis de
hierarquia por cena.

**Cor de destaque.** Âmbar `#e8a33d`, com moderação: uma palavra, um badge,
um detalhe. A maior parte da peça fica neutra.

## 7. Legenda

Quem assiste sem som precisa entender o vídeo.

- Legenda editorial compacta, nunca uma caixa preta de largura total.
- Largura de 55% a 70% do quadro (até 720 px), altura mínima, cantos de 18 a 22 px, sombra muito suave.
- Fundo escuro translúcido: `rgba(22,19,16,0.86)` com `backdrop-filter: blur(14px)`. Texto creme. Contraste mínimo de 4,5:1.
- Posição fixa em todas as cenas: abaixo do painel, entre y 1280 e y 1500. Nunca em cima da interface.
- Frase curta. "Ainda usa vários sistemas?", não "Sua empresa ainda usa vários sistemas separados?".
- No máximo uma expressão destacada por frase, em âmbar. Com legenda palavra por palavra, o destaque é a palavra falada.

## 8. Movimento

O vídeo não pode parecer uma sequência de imagens paradas. O movimento é
sutil: quem assiste sente profundidade sem reparar na animação.

- Use: câmera aproximando devagar (zoom de 4% a 12%), parallax discreto, fade, slide de poucos pixels, scale suave. Transições de 200 a 500 ms.
- Não use: bounce, shake, zoom agressivo, elementos pulando, transição chamativa, movimento rápido.
- A cada 1,5 a 3 s acontece uma mudança visual pequena: aproximação, reposicionamento ou troca de foco.
- Cada cena comunica uma ideia. Alterne visão geral, close da funcionalidade, interação e resultado.

Para demonstrar uma funcionalidade:

1. Mostre rápido o contexto da tela.
2. Leve a câmera até a funcionalidade.
3. Amplie de 8% a 15%.
4. Escureça de leve as regiões secundárias.
5. Execute a ação real.
6. Mostre o resultado.

Sem círculos, setas ou marcações. A câmera conduz o olhar.

## 9. Encerramento

A interface sai aos poucos. Ficam só a logo do Nallon (ou o nome NALLON) e a
frase "Gestão inteligente para o seu negócio.", centralizadas sobre o fundo.
A marca entra com animação discreta, de 0,8 a 1,5 s, e a cena dura até a
fala da assinatura terminar. Sem CTA, sem efeito luminoso.

## 10. Revisão antes de exportar

- Quadro em 9:16, sem barras pretas.
- Título, logo e painel inteiros em x 65–1015, y 270–1240; legenda entre y 1280 e y 1500. A folha de conferência do `producao.md` (`zona-segura.jpg`) mostra isso de uma vez.
- Em nenhum quadro a legenda encosta na interface.
- Capa no modelo fixo da seção 1.
- Alinhamentos, margens e espaçamentos consistentes.
- Interface nítida e legível; proporção e sombra do painel coerentes entre as cenas.
- Legenda sincronizada, compacta e com um destaque só.
- Ritmo: nenhuma cena parada por mais de 3 s.
- Encerramento limpo, com a assinatura exata.

Se parecer template, tire elementos. A qualidade vem de composição,
tipografia, movimento e interface real.

## Fontes

Conferido em 2026-10-03. Reveja quando o Instagram mudar o app.

- Central de Ajuda do Instagram, "Tamanho e taxas de proporção de reels": https://help.instagram.com/1038071743007909
- Guia de anúncios da Meta, Instagram Reels (zona segura e codec): https://www.facebook.com/business/ads-guide/update/video/instagram-reels
