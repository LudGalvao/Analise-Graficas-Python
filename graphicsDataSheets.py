import os.path
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
import pandas as pd
import matplotlib.pyplot as plt


# ID da Planilha do Google Sheets
ID_PLANILHA = ""  # Insira o ID da sua planilha aqui

def obter_entrada(mensagem):
    valor = input(mensagem + ": ")
    return valor.strip()

def obter_dados_google_sheets():
    credenciais = None

    if os.path.exists("token.json"):
        credenciais = Credentials.from_authorized_user_file("token.json")

    if not credenciais or not credenciais.valid:
        if credenciais and credenciais.expired and credenciais.refresh_token:
            credenciais.refresh(Request())
        else:
            fluxo = InstalledAppFlow.from_client_secrets_file(
                "client_secrets.json",
                ["https://www.googleapis.com/auth/spreadsheets.readonly"],
            )
            credenciais = fluxo.run_local_server(port=0)

        with open("token.json", "w") as token:
            token.write(credenciais.to_json())

    servico = build("sheets", "v4", credentials=credenciais)
    planilha = servico.spreadsheets()

    range_nome = obter_entrada("Digite o nome da range dos dados: ")
    resultado = (
        planilha.values().get(spreadsheetId=ID_PLANILHA, range=range_nome).execute()
    )
    valores = resultado.get("values", [])

    if not valores:
        print("Nenhum dado encontrado.")
        return None

    return pd.DataFrame(valores[1:], columns=valores[0])

def analisar_dados():
    try:
        df = obter_dados_google_sheets()
        if df is None:
            return

        print("Colunas da planilha: ")
        for coluna in df.columns:
            print(coluna)

        eixo_x = input("Escolha a coluna para o eixo x: ")
        eixo_y = input("Escolha a coluna para o eixo y: ")
        tipo_grafico = input("Informe o tipo de gráfico (Linhas, Barras, Dispersão): ")

        if eixo_x not in df.columns or eixo_y not in df.columns:
            print("A coluna não existe ou foi digitada incorretamente.")
            return

        if tipo_grafico.lower() in ["barras", "linhas"]:
            df.plot(x=eixo_x, y=eixo_y, kind=tipo_grafico.lower())
            plt.xlabel(eixo_x)
            plt.ylabel(eixo_y)
            plt.title(f'Gráfico de {tipo_grafico.capitalize()}')
            plt.show()
        elif tipo_grafico.lower() == "dispersão":
            df.plot(kind='scatter', x=eixo_x, y=eixo_y)
            plt.xlabel(eixo_x)
            plt.ylabel(eixo_y)
            plt.title('Gráfico de Dispersão')
            plt.show()
        else:
            print("Tipo de gráfico não reconhecido.")

    except Exception as e:
        print("Ocorreu um erro ao analisar os dados:", e)

if __name__ == "__main__":
    analisar_dados()
