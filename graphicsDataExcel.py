import pandas as pd
import matplotlib.pyplot as plt

def analisar_dados():
    # Endereço da planilha excel
    arquivo = 'BaseFuncionarios.xlsx'

    try:
        df = pd.read_excel(arquivo)
    
    except FileNotFoundError:
        print("Arquivo excel não encontrado")
        return
    
    print("Colunas da planilha: ")
    for coluna in df.columns:
        print(coluna)

    eixo_x = input("Escolha a coluna para o eixo x: ")

    eixo_y = input("Escolha a coluna para o eixo y: ")

    tipo_graficos = input("Informe o tipo de grafico(Linhas, barras, dispersão): ")

    if eixo_x not in df.columns or eixo_y not in df.columns:
        print("A Coluna não existe ou foi digitada errada")
        return

    if tipo_graficos in ["barras", "linhas"]:
        df.plot(x=eixo_x, y=eixo_y, kind=tipo_graficos)
        plt.xlabel(eixo_x)
        plt.ylabel(eixo_y)
        plt.title(f'Gráfico de {tipo_graficos.capitalize()}')
        plt.show()
    elif tipo_graficos == "dispersão":
        df.plot(kind='scatter', x=eixo_x, y=eixo_y)
        plt.xlabel(eixo_x)
        plt.ylabel(eixo_y)
        plt.title('Gráfico de Dispersão')
        plt.show()
    else:
        print("Tipo de gráfico não reconhecido")


    plt.show()

analisar_dados()
