# Projeto de Análise de Arte

Este é um projeto para análise de arte que utiliza a biblioteca Tesseract para extrair informações de imagens e PDFs. O projeto contém uma classe chamada "arte" que pode ler informações de um arquivo PDF contendo chaves de verificação de arte e analisar a conformidade de uma imagem com essas chaves.

## Requisitos

Certifique-se de ter os seguintes requisitos instalados em seu sistema antes de executar o projeto:

- Python 3.x
- Tesseract OCR

## Instalação

1. Clone este repositório em seu computador:

```bash
git clone 
```

Acesse o diretório do projeto:

```bash
cd projeto-analise-arte
```


Crie um ambiente virtual (opcional, mas recomendado):
```bash
python -m venv venv

```

Ative o ambiente virtual (Linux/macOS):
```bash
source venv/bin/activate
```
Instale as dependências do projeto:
```bash
pip install -r requirements.txt
```

## Configuração

Baixe o arquivo "por.traineddata" para o Tesseract. Você pode obtê-lo no repositório oficial do Tesseract no GitHub: https://github.com/tesseract-ocr/tessdata. Baixe o arquivo "por.traineddata" e coloque-o em um diretório de dados do Tesseract em seu sistema. Lembre-se do caminho para este diretório, pois você precisará configurar a variável de ambiente TESSDATA_PREFIX.

Configure a variável de ambiente TESSDATA_PREFIX para apontar para o diretório que contém os arquivos de treinamento de idioma. Por exemplo:
Linux/macOS:


```bash

export TESSDATA_PREFIX=/caminho/para/seus/arquivos/tessdata/
```


## Execução
Agora você pode executar o projeto:
```bash

python main.py
```

O projeto deve ser executado sem erros e utilizará o arquivo "por.traineddata" para extrair informações da imagem ou PDF.

