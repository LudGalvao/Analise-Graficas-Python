# Analise-Graficas-Python

Uma ferramenta em Python para facilitar a criação de graficos usando a biblioteca Matplotlib.

## Ferramentas Utilizadas

- **google-auth**: Biblioteca para autenticação com as APIs do Google.
- **google-auth-oauthlib**: Biblioteca para fluxos de autenticação OAuth2 com o Google.
- **googleapiclient**: Biblioteca para interagir com as APIs do Google.
- **Pandas** para ler as planilhas
- **Matplotlib** para a criação dos graficos

## Pré-requisitos

Certifique-se de ter o pip das bibliotecas e a versão correta do Python instalados.

### Instalação do pip do Google(Caso esteja usando a versão do google sheets)

```
pip install google-auth google-auth-oauthlib google-api-python-client
```

### Instalação do pip do Pandas
```
pip install pandas
```

### Instalação do pip do Matplotlib
```
pip install matplotlib
```


## Configuração para a versão com Sheets

Antes de começar, é necessário configurar as credenciais de autenticação com o Google.

1. Crie um projeto no [Google Cloud Console](https://console.cloud.google.com/).
2. Ative a API do Google Sheets para o seu projeto.
3. Crie um arquivo de credenciais JSON para o tipo de autenticação que deseja utilizar (por exemplo, OAuth2).
4. Renomeie o arquivo de credenciais para `credentials.json` e coloque-o no diretório raiz do projeto.

## Uso

Execute o script `.py` para inserir dados na planilha do Google Sheets.

```bash
python NomeDoProjeto.py
