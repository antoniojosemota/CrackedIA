# CrackedIA

O **CrackedIA** é uma ferramenta baseada em Inteligência Artificial para detecção automática de rachaduras em imagens de superfícies. O projeto utiliza um modelo de Deep Learning (Keras/TensorFlow) para processar imagens e destacar visualmente as áreas danificadas.

## 📋 Funcionalidades

- Carregamento de modelos de rede neural no formato `.keras`.
- Pré-processamento automático de imagens (redimensionamento e normalização).
- Geração de máscaras binárias de segmentação para identificar falhas.
- Visualização em tempo real:
  - Imagem Original.
  - Máscara Prevista (preto e branco).
  - Overlay (rachaduras destacadas em vermelho sobre a imagem original).

## 🛠️ Tecnologias Utilizadas

- **Python**
- **TensorFlow / Keras**: Para carregamento e inferência do modelo de IA.
- **OpenCV (cv2)**: Para manipulação de imagens e visualização dos resultados.
- **NumPy**: Para operações matriciais e processamento dos dados.

## 🚀 Como Usar

### Pré-requisitos
Certifique-se de ter o Python instalado e as bibliotecas necessárias:

```bash
pip install tensorflow opencv-python numpy
```

## Executando a Detecção
 Coloque o arquivo do modelo treinado (crack_detection2.keras) e a imagem a ser analisada (piso.jpg) no diretório raiz do projeto.

 Execute o script de teste:

```bash
python cracktest.py
```
