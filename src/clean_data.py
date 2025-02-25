import pandas as pd
import ast  # Para converter strings com listas em listas reais
import re
import unicodedata
from collections import Counter


def carregar_dados(caminho):
    """
    Função para carregar o dataset a partir de diferentes tipos de arquivo,
    como CSV, Excel, Parquet, JSON e outros formatos suportados pelo pandas.
    A função detecta automaticamente o tipo de arquivo com base na extensão.
    """
    # Obter a extensão do arquivo
    extensao = caminho.split('.')[-1].lower()

    if extensao == 'csv':
        return pd.read_csv(caminho)
    elif extensao == 'xlsx' or extensao == 'xls':
        return pd.read_excel(caminho)
    elif extensao == 'json':
        return pd.read_json(caminho)
    elif extensao == 'parquet':
        return pd.read_parquet(caminho)
    else:
        raise ValueError(f"Extensão '{extensao}' não suportada. Suporte para CSV, Excel, JSON e Parquet.")



def tratar_respostas_multiescolha(df, coluna):
    """
    Trata uma coluna de múltipla escolha transformando os valores em listas padronizadas
    e criando colunas binárias para cada opção única.
    """
    # Mapeamento de caracteres quebrados para correção
    mapeamento_correcao = {
        "\u00d4nibus": "Ônibus",
        "\u00ea": "ê",
        "\u00e1": "á",
        "\u00e9": "é",
        "\u00ed": "í",
        "\u00f3": "ó",
        "\u00fa": "ú",
        "\u00e0": "à",
        "\u00f1": "ñ",
        "\u00e3": "ã",
        "\u00f5": "õ",
        "\u00e7": "ç",
        "\u00c1": "Á",
        "\u00c9": "É",
        "\u00cd": "Í",
        "\u00d3": "Ó",
        "\u00da": "Ú",
        "\u00c0": "À",
        "\u00c3": "Ã",
        "\u00d5": "Õ",
        "\u00c7": "Ç",
        "\u00f4": "ô",
        "\u00fb": "û",
        "\u00ea": "ê",
        "\u00f2": "ò",
        "\u00e2": "â",
        "\u00ea": "ê",
        "\u00f4": "ô",
        "\u00fb": "û"
    }

    def limpar_resposta(valor):
        if isinstance(valor, str):
            try:
                for k, v in mapeamento_correcao.items():
                    valor = valor.replace(k, v)
                
                if valor.startswith("[") and valor.endswith("]"):
                    valor = ast.literal_eval(valor)
                else:
                    valor = valor.split(", ")
            except:
                valor = [valor]
        elif pd.isna(valor):
            valor = []
        return [item.strip() for item in valor]

    df[coluna] = df[coluna].apply(limpar_resposta)
    
    todas_opcoes = set(item for sublist in df[coluna] for item in sublist)
    for opcao in todas_opcoes:
        df[opcao] = df[coluna].apply(lambda x: 1 if opcao in x else 0)
    
    return df

def padronizar_dados(df, coluna, categorias_validas=None):
    """
    Padroniza os valores de uma coluna substituindo valores atípicos pelos valores mais frequentes.
    Se uma lista de categorias válidas for fornecida, os valores divergentes serão substituídos pelo mais frequente.
    """
    valores_unicos = df[coluna].dropna().unique()
    
    if categorias_validas is None:
        contagem = Counter(df[coluna].dropna())
        categorias_validas = set(contagem.keys())
    
    valor_mais_frequente = df[coluna].mode()[0]
    
    def limpa_valor(valor):
        if pd.isna(valor) or valor in categorias_validas:
            return valor
        return valor_mais_frequente
    
    df[coluna] = df[coluna].apply(limpa_valor)
    return df

def padronizar_binarios(df, coluna):
    """
    Converte valores booleanos e binários para 0 e 1.
    """
    mapeamento = {
        'True': 1, 'False': 0,
        '1': 1, '0': 0,
        'Sim': 1, 'Não': 0,
        'Yes': 1, 'No': 0,
        'Y': 1, 'N': 0
    }
    
    df[coluna] = df[coluna].astype(str).str.strip().map(lambda x: mapeamento.get(x, x)).astype(int)
    return df

def tratar_datas(df, colunas_data):
    """
    Trata colunas de data, corrigindo erros de formatação e removendo datas inválidas.
    """
    datas_invalidas = ['1900-01-01 00:00:00', '2210-07-15 18:16:26']
    
    for coluna in colunas_data:
        df[[coluna, 'zeros']] = df[coluna].astype(str).str.split('.', expand=True).iloc[:, :2]
        df[coluna] = pd.to_datetime(df[coluna], errors='coerce')
        df = df[~df[coluna].astype(str).isin(datas_invalidas)]
    
    erro_1900 = (df[colunas_data].astype(str) == '1900-01-01 00:00:00').sum().sum()
    erro_2210 = (df[colunas_data].astype(str) == '2210-07-15 18:16:26').sum().sum()
    
    print(f"Total de datas com erro '1900-01-01 00:00:00': {erro_1900}")
    print(f"Total de datas com erro '2210-07-15 18:16:26': {erro_2210}")
    
    return df

def criar_faixa_etaria(df, coluna_data_nascimento):
    """
    Cria uma coluna de faixa etária a partir da coluna de data de nascimento.
    """
    formatos_tentativa = ['%Y-%m-%d', '%d/%m/%Y', '%m/%d/%Y', '%d-%m-%Y', '%Y/%m/%d']
    
    for formato in formatos_tentativa:
        df[coluna_data_nascimento] = pd.to_datetime(df[coluna_data_nascimento], format=formato, errors='coerce')
        if df[coluna_data_nascimento].notna().sum() > 0:
            break
    
    df = df.dropna(subset=[coluna_data_nascimento])
    df['idade'] = (pd.to_datetime('today') - df[coluna_data_nascimento]).dt.days // 365
    
    bins = [0, 17, 29, 44, 59, 100]
    labels = ['0-17 anos', '18-29 anos', '30-44 anos', '45-59 anos', '60+ anos']
    df['faixa_etaria'] = pd.cut(df['idade'], bins=bins, labels=labels, right=True)
    
    return df
