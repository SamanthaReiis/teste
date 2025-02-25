import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np


def analisar_dados(df):
    """
    Exibe informações gerais sobre os dados, como tipos e valores nulos.
    """
    print("Informações gerais sobre os dados:")
    df.info()
    
    print("\nContagem de valores nulos por coluna:")
    print(df.isnull().sum())

def distribuicao_variaveis_categoricas(df, categorias=None, plot=False):
    """
    Exibe a distribuição das variáveis categóricas e, opcionalmente, plota gráficos.
    """
    if categorias is None:
        categorias = df.select_dtypes(include=['object', 'category']).columns.tolist()
    
    for categoria in categorias:
        print(f"\nDistribuição de {categoria}:")
        print(df[categoria].value_counts())
        
        if plot:
            plt.figure(figsize=(8, 6))
            sns.countplot(data=df, x=categoria, order=df[categoria].value_counts().index)
            plt.title(f'Distribuição de {categoria}')
            plt.xticks(rotation=45, ha='right')
            plt.tight_layout()
            plt.show()

def verificar_outliers(df, colunas):
    """
    Verifica a presença de outliers nas colunas numéricas com boxplots.
    """
    for coluna in colunas:
        plt.figure(figsize=(8,6))
        sns.boxplot(x=df[coluna])
        plt.title(f'Boxplot de {coluna}')
        plt.show()


def calcular_limites_iqr(df, colunas):
    """
    Função para calcular os limites inferior e superior com base no IQR (intervalo interquartil).
    Retorna um dicionário com limites para cada coluna numérica.
    """
    limites = {}
    for coluna in colunas:
        Q1 = df[coluna].quantile(0.25)
        Q3 = df[coluna].quantile(0.75)
        IQR = Q3 - Q1
        
        limite_inferior = Q1 - 1.5 * IQR
        limite_superior = Q3 + 1.5 * IQR
        limites[coluna] = (limite_inferior, limite_superior)
    
    return limites


def tratar_outliers(df, colunas, limites=None):
    """
    Função para tratar outliers em colunas numéricas.
    Substitui valores fora dos limites definidos por NaN.
    
    Se os limites não forem fornecidos, será usado o IQR para calcular automaticamente.
    """
    # Se os limites não forem fornecidos, calcular os limites com base no IQR
    if limites is None:
        limites = calcular_limites_iqr(df, colunas)
    
    # Substitui valores fora dos limites por NaN
    for coluna, (limite_inferior, limite_superior) in limites.items():
        df[coluna] = df[coluna].apply(lambda x: np.nan if (x < limite_inferior or x > limite_superior) else x)
    
    return df


def verificar_datas(df, colunas_datas):
    """
    Converte colunas de data e exibe o intervalo de datas.
    """
    intervalo_datas = {}
    for coluna in colunas_datas:
        df[coluna] = pd.to_datetime(df[coluna], errors='coerce')
        intervalo_datas[coluna] = (df[coluna].min(), df[coluna].max())
    return intervalo_datas

def cruzar_variaveis(df, var1, var2, plot=False):
    """
    Exibe a relação entre duas variáveis categóricas.
    """
    print(f"\nTabela cruzada entre {var1} e {var2}:")
    tabela_cruzada = pd.crosstab(df[var1], df[var2])
    print(tabela_cruzada)
    
    if plot:
        plt.figure(figsize=(10,6))
        sns.heatmap(tabela_cruzada, annot=True, fmt="d", cmap="Blues")
        plt.title(f"Cruzamento entre {var1} e {var2}")
        plt.show()

def agregar_dados(df, grupo, agregacao):
    """
    Agrega dados por uma variável categórica e exibe estatísticas.
    """
    print(f"\nAgregação de dados para {grupo}:")
    print(df.groupby(grupo).agg(agregacao))
    return df.groupby(grupo).agg(agregacao).reset_index()

def correlacao_variaveis_numericas(df, plot=False):
    """
    Calcula e exibe a correlação entre variáveis numéricas.
    """
    correlacao = df.corr()
    print("\nMatriz de correlação:")
    print(correlacao)
    
    if plot:
        plt.figure(figsize=(10,8))
        sns.heatmap(correlacao, annot=True, cmap='coolwarm', fmt='.2f')
        plt.title("Matriz de Correlação")
        plt.show()
    
    return correlacao


def verificar_duplicatas(df, coluna_id):
    """
    Verifica a quantidade de ocorrências de cada ID e adiciona colunas indicando duplicação e contagem de ocorrências.

    Parâmetros:
    - df: DataFrame contendo os dados.
    - coluna_id: Nome da coluna na qual verificar duplicações.

    Retorna:
    - DataFrame atualizado com:
      - 'duplicado': 1 se houver duplicações, 0 caso contrário.
      - 'frequencia_id': Número total de vezes que cada ID aparece no dataset.
    """
    # Criar coluna com contagem de ocorrências do ID
    df['frequencia_id'] = df[coluna_id].map(df[coluna_id].value_counts())

    # Criar coluna binária indicando se é duplicado (aparece mais de uma vez)
    df['duplicado'] = (df['frequencia_id'] > 1).astype(int)

    # Exibir informações
    print(f"Total de IDs únicos: {df[coluna_id].nunique()}")
    print(f"Total de IDs duplicados: {df['duplicado'].sum()}")
    
    return df
