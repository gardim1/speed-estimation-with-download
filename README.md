# Fan Camera - Detecção de Velocidade de Carros de Fórmula E com YOLOv8

<img src="https://miro.medium.com/v2/resize:fit:720/format:webp/1*J-xFM5IGIsRwBvpDXbqjJQ.png" alt="Logo formulaE" width = "1000"/>

## Descrição do Projeto

**Fan Camera** é um projeto desenvolvido para fãs de Fórmula E, permitindo que eles assistam às corridas e visualizem em tempo real a velocidade dos carros. Utilizando um modelo de detecção de objetos baseado no **YOLOv8**, a Fan Camera processa vídeos gravados ou transmissões ao vivo e exibe as bounding boxes ao redor dos carros com a velocidade estimada, funcionando como uma espécie de "câmera-radar".

Este projeto foi desenvolvido por um grupo de estudantes de engenharia de software, com o objetivo de aplicar técnicas de visão computacional para criar uma ferramenta interativa para o público.

<img src="https://miro.medium.com/v2/resize:fit:720/format:webp/1*YQWYPi4uoT8RcG6BPbUoVw.png" alt="Logo YOLOv8" width = "1000"/>

## Funcionalidades

- **Detecção em Tempo Real**: Processa vídeos ao vivo ou gravados.
- **Cálculo de Velocidade**: Detecta os carros de Fórmula E e calcula a velocidade com base na posição dos objetos entre frames.
- **Bounding Boxes Customizadas**: Exibe a velocidade dos carros diretamente nas caixas delimitadoras (bounding boxes) em vez de nomes ou outros dados.
- **Processamento de Vídeos**: Salva os vídeos processados com as informações de velocidade diretamente nas imagens.

## Como o Código Funciona

1. **Carregamento do Modelo YOLOv8**: O código carrega um modelo YOLOv8 pré-treinado que detecta carros de Fórmula E. O modelo é carregado de um arquivo `.pt`, onde ele foi previamente treinado em um conjunto de dados de carros de Fórmula E.

2. **Processamento do Vídeo**: O código usa a biblioteca OpenCV para capturar o vídeo. Esse vídeo pode ser ao vivo, capturado de uma câmera, ou um arquivo de vídeo gravado previamente.

3. **Detecção de Objetos**: Para cada frame do vídeo, o modelo YOLOv8 detecta os carros no frame, gerando caixas delimitadoras (bounding boxes) ao redor dos carros. Essas caixas incluem coordenadas, confiabilidade da detecção e a classe do objeto.

4. **Cálculo de Velocidade**: A velocidade de cada carro é calculada comparando a posição do carro em frames consecutivos. A fórmula de cálculo usa a distância entre as posições nos frames, a escala do vídeo (em metros por pixel) e a taxa de frames por segundo (FPS) do vídeo.

5. **Exibição das Bounding Boxes**: As bounding boxes ao redor dos carros são desenhadas no vídeo, e a velocidade de cada carro é exibida diretamente na tela, dentro da caixa delimitadora, com uma cor personalizada.

6. **Gravação do Vídeo**: O vídeo processado é gravado em um arquivo de saída, com as informações de velocidade visíveis em cada frame.

## Requisitos

- Python 3.x
- Bibliotecas:
  - OpenCV (`pip install opencv-python`)
  - Ultralytics YOLOv8 (`pip install ultralytics`)
  - NumPy (`pip install numpy`)

## Como Executar

1. Clone este repositório ou baixe os arquivos necessários.
2. Certifique-se de que você tenha o modelo YOLOv8 treinado (arquivo `.pt`) e o vídeo de entrada.
3. Configure os caminhos para o modelo e o vídeo de entrada no código.
4. Instale as dependências necessárias:
```bash
pip install ultralytics
```
5. Execute o código:

```bash
python fan_camera.py
```
## Exemplo de Uso

O **Fan Camera** pode ser usada para analisar corridas de Fórmula E e fornecer aos fãs uma nova maneira de acompanhar as competições. Veja, em tempo real ou em vídeos gravados, a velocidade dos carros enquanto eles percorrem a pista. A interface exibe as bounding boxes ao redor dos carros com a velocidade calculada diretamente sobre os vídeos.


## Como Funciona o Cálculo de Velocidade?

A velocidade dos carros é calculada com base na diferença de posição entre dois frames consecutivos:

- O código calcula a distância percorrida em pixels e converte essa distância para metros usando um fator de escala pré-definido (em metros por pixel).
- Em seguida, a distância é multiplicada pelo FPS (frames por segundo) do vídeo para calcular a velocidade em metros por segundo.
- Finalmente, a velocidade é convertida de metros por segundo para quilômetros por hora (km/h) usando um fator de conversão.

## Detalhe

Este é um projeto acadêmico feito na instituição FIAP em conjunto com a empresa e montadora de carros de Fórmula E Mahindra.

<img src="https://store.fiaformulae.com/on/demandware.static/-/Sites-navigation-catalog-FE-S9/default/dw8427c471/LogosTeams/LogoMahindra2.png" alt="Logo Mahindra" width="300"/><img src="https://play-lh.googleusercontent.com/qRAt8XQzsRcEG7LGb7dwOBTuNocOV-lokZjZot4xwIv6wDfgAeFFB5HKkKb8VqZhHNc=w240-h480-rw" alt="Logo formulaE2" width="200"/> <img src="https://avatars.githubusercontent.com/u/79948663?s=200&v=4" alt="Logo FIAP" width="200"/>


Equipe E-fficency:

Camila Feitosa RM: 558808

Gabriel Matiolli RM: 558963

Gustavo Berlanga RM: 555298

Leonardo Taschin RM: 554583

Vinicius Gardim RM: 556013


