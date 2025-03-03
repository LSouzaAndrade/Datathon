# Datathon - Grupo 12 - 1MLET

## 🚀 Sobre o projeto 

### Objetivos do Datathon
Este projeto foi desenvolvido para o Datathon da Pós Tech de Engenharia de Machine Learning da FIAP em parceria com a Globo.com, cujo objetivo é desenvolver um modelo de sistema de recomendação personalizada para cada usuário com base nos dados de notícias do G1, predizendo qual será a próxima notícia que ele vai ler.
O Modelo deve considerar o problema relacionado a cold-start e o conceito de recência para as recomendações.

## 📝 Arquitetura do Projeto

A estrutura de pastas e arquivos do projeto se encontra disposta da seguinte maneira:

```bash
├── api                                     # Diretório de arquivos da API
    ├── app                                 # Diretório de arquivos da aplicação da API
        ├── auxiliar                        # Diretório de dependências da aplicação da API
            ├── processed_itens.parquet     # Dataframe de notícias tratadas para uso no modelo
            ├── tfidf_matrix.pkl            # Matriz de vetores TF-IDF das notícias processadas
            └── tfidf_vocab.pkl             # Vocabulário do corpo textual TF-IDF
        ├── pydantic_models                 # Diretório de modelos de validação de dados
            └── models.py                   # Modelos de validação de dados
        ├── routers                         # Diretório de endpoints da API
            ├── healthcheck.py              # Endpoint de healthcheck da API
            ├── recommendation.py           # Endpoint de recomendações de notícias
            └── root.py                     # Redirecionamento para documentação da API
        └── api.py                          # Estrutura da API
    ├── Dockerfile                          # Arquivo de configuração da imagem Docker
    ├── requirements.txt                    # Dependências externas utilizadas
    └── run.py                              # Script de inicialização do servidor para API
├── convert_kaggle.py                       # Arquivo do dataset original do Datathon
├── notebook.ipynb                          # Notebook (EDA e treinamento dos modelos)
├── test_top10_submission.csv               # Arquivo do dataset original do Datathon
├── topk.py                                 # Arquivo do dataset original do Datathon
└── validacao.pcsv                          # Arquivo do dataset original do Datathon 

```
Devido a restrição do tamanho máximo para arquivos no repositório, os arquivos do diretório "auxiliar" se encontram em: https://drive.google.com/drive/u/0/folders/12dl4JVzO7wL79IacuM8WCnP3bkoricjl

## 📋 Pré-requisitos
Para utilização da API para os modelos gerados neste projeto, se fazem necessárias as dependências contidas no arquivo requirements.txt.

## 🔧 Instalação
Todas dependências necessárias para reprodução do projeto contido neste repositório foram testadas com a versão 3.12.5 do Python. \
É recomendado que sejam utilizadas as versões de dependências incluídas no arquivo [requirements.txt](requirements.txt), a fim de evitar erros originados por incompatibilidade de versões.


```bash
# Crie a imagem do Docker:
docker build -t nome-imagem .

# Inicie o container com a imagem Docker criada:
docker run -d -p 8000:8000 nome-imagem
```

## ⚙️ Execução
Em caso de execução direta, com ambiente virtual ativo, utilize:

### Uvicorn
```bash
# Inicie o servidor Uvicorn para execução do FastAPI:
# (Por padrão, o Uvicorn irá rodar na porta 8000)
python run.py
```

Em caso de uso de Docker:

### Docker
```bash
# Inicie o container com a imagem Docker criada:
docker run -d -p 8000:8000 nome-imagem
```

Após o servidor da API estar em execução, é possível realizar requisições para API. \
Sendo necessária a seguinte estrutura de payload para realizar a request à API:
```bash
{
    "historico": array[str],        # Array de IDs das noticias acessadas
    "timestamp": int                # Timestamp Unix em segundos do momento do acesso
}
 
```

## ✒️ Autores

Isabelli Andrade de Souza - https://github.com/Isabellitankian
<br>
Lucas Souza Andrade dos Santos - https://github.com/LSouzaAndrade
<br>
Michel de Lima Maia - https://github.com/Michel-Maia
<br>
Valquiria Rodrigues de Oliveira Pires - https://github.com/KyraPires