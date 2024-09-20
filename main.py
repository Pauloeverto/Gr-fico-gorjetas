# Importar as bibliotecas necessárias
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

ex01 = "Data/gorjetas.xlsx"
# Exercicio 01
def exercicio(ex01):
    # Carregar o arquivo Excel
    df = pd.read_excel("Data/gorjetas.xlsx", sheet_name='Gorjetas')

    # Limpando os dados - Convertendo colunas 'total_conta' e 'gorjeta' para numéricas e removendo dados inválidos
    df['gorjeta'] = pd.to_numeric(df['gorjeta'], errors='coerce')
    df = df.dropna(subset=['gorjeta'])  # Remover valores nulos na coluna 'gorjeta'

    # Criando o gráfico de densidade das gorjetas por sexo
    plt.figure(figsize=(10, 6))
    sns.kdeplot(data=df, x='gorjeta', hue='sexo', fill=True)

    # Adicionando título e rótulos
    plt.title('Gráfico de Densidade das Gorjetas por Sexo')
    plt.xlabel('Gorjeta')
    plt.ylabel('Densidade')

    # Mostra o gráfico
    plt.show()

#EXERCICIO 01
exercicio(ex01)
 

# Exercicio 02
def exercicio(ex02):
    # Carregar o arquivo Excel
    df = pd.read_excel(ex02, sheet_name='Gorjetas')

    # Limpar os dados - Convertendo colunas 'gorjeta' e 'quantidade' para numéricas e removendo dados inválidos
    df['gorjeta'] = pd.to_numeric(df['gorjeta'], errors='coerce')
    df['quantidade'] = pd.to_numeric(df['quantidade'], errors='coerce')
    df = df.dropna(subset=['gorjeta', 'quantidade'])  # Remove valores nulos nas colunas relevantes

    # Criando o gráfico de densidade do total de gorjetas pela quantidade de pessoas na mesa
    plt.figure(figsize=(10, 6))
    sns.kdeplot(data=df, x='gorjeta', hue='quantidade', fill=True, palette='viridis')

    # Adicionando título e rótulos
    plt.title('Gráfico de Densidade das Gorjetas pela Quantidade de Pessoas na Mesa')
    plt.xlabel('Gorjeta')
    plt.ylabel('Densidade')

    # Mostra o gráfico
    plt.show()

# Exemplo de chamada da função
ex02 = 'Data/gorjetas.xlsx'
exercicio(ex02)



# Exercicio 03
def exercicio(ex03):
    # Carregar o arquivo Excel
    df = pd.read_excel(ex03, sheet_name='Gorjetas')

    # Limpando os dados - Convertendo a coluna 'gorjeta' para numérico e removendo dados inválidos
    df['gorjeta'] = pd.to_numeric(df['gorjeta'], errors='coerce')
    df = df.dropna(subset=['gorjeta', 'dia'])  # Remove valores nulos nas colunas relevantes

    # Criando o gráfico de densidade do total de gorjetas por dia da semana
    plt.figure(figsize=(10, 6))
    sns.kdeplot(data=df, x='gorjeta', hue='dia', fill=True, palette='Set2')

    # Adicionando título e rótulos
    plt.title('Gráfico de Densidade das Gorjetas por Dia da Semana')
    plt.xlabel('Gorjeta')
    plt.ylabel('Densidade')

    # Mostrar o gráfico
    plt.show()


ex03 = 'Data/gorjetas.xlsx'
exercicio(ex03)



