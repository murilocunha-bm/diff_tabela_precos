#!.venv/bin/python3
# -*- coding: utf-8 -*-


import pandas as pd
from os import path
from datetime import datetime
from . import PASTA_XLS, XLS_TABELA_PRECO, XLS_PRECO_NOVO


def carregar_tabela(linhas_pular: int, colunas_ler:str, linhas_ler: int):
    try:
        df = pd.read_excel(
            path.join(PASTA_XLS, XLS_TABELA_PRECO),
            # engine='openpyxl'                 # Use 'openpyxl' para arquivos .xlsx
            engine = 'xlrd',                    # Use 'xlrd' para arquivos .xls
            skiprows = linhas_pular,            # Pula as linhas especificadas
            usecols = colunas_ler,              # Ou use nomes das colunas: ['Coluna1', 'Coluna2']
            nrows = linhas_ler                  # Lê apenas as próximas linhas especificadas
        )
        df.columns = [                          # Renomeia as colunas
            'Codigo',
            'Produtos',
            'PesoCaixa',
            'R$',
        ]
        for col in ['PesoCaixa']:               # Se quiser remover 'kg' de uma coluna específica
            df.loc[df.index[0:], col ] = (      
                df.loc[df.index[0:], col ]
                .astype(str)
                .str.replace('kg', '', regex=False)
                .str.strip()
            )
        df = df.astype(
            {
                'Codigo': int,
                'Produtos': str,
                'PesoCaixa': float,
                'R$': float,
            }
        )
    except Exception as e:
        df = pd.DataFrame(columns=['Codigo', 'Produtos', 'PesoCaixa', 'R$'])
        print(f"[ {datetime.now().strftime('%d/%m/%Y %H:%M:%S')} - ERRO ] Não foi possível carregar a tabela de preços. {e.args}")

    return df


def montar_tabela_unica():
    """Montar uma tabela única com os dados de várias tabelas."""   
    # Carrega as tabelas
    df1 = carregar_tabela(linhas_pular=5, colunas_ler='C:F', linhas_ler=46)
    df2 = carregar_tabela(linhas_pular=53, colunas_ler='C:F', linhas_ler=10)
    df3 = carregar_tabela(linhas_pular=65, colunas_ler='C:F', linhas_ler=4)
    df4 = carregar_tabela(linhas_pular=5, colunas_ler='H:K', linhas_ler=6)
    df5 = carregar_tabela(linhas_pular=13, colunas_ler='H:K', linhas_ler=6)
    df6 = carregar_tabela(linhas_pular=21, colunas_ler='H:K', linhas_ler=17)
    df7 = carregar_tabela(linhas_pular=40, colunas_ler='H:K', linhas_ler=3)
    df8 = carregar_tabela(linhas_pular=45, colunas_ler='H:K', linhas_ler=6)
    df9 = carregar_tabela(linhas_pular=53, colunas_ler='H:K', linhas_ler=6)
    df10 = carregar_tabela(linhas_pular=61, colunas_ler='H:K', linhas_ler=3)
    df11 = carregar_tabela(linhas_pular=66, colunas_ler='H:K', linhas_ler=4)

    # Se quiser juntar lado a lado (colunas), use axis=1
    df_todos = pd.concat(
        [df1, df2, df3, df4, df5, df6, df7, df8, df9, df10, df11], 
        ignore_index=True,
        axis=0
    )
    # Ordena pela coluna
    df_todos = df_todos.sort_values(by='Codigo', ascending=True)

    # Remove linhas onde o valor de R$ é 0
    df_todos = df_todos[df_todos['R$'] != 0]

    # Salva o DataFrame em um arquivo Excel para comferencia manual
    xlsx_salvo = path.join(PASTA_XLS, XLS_PRECO_NOVO)
    df_todos.to_excel(xlsx_salvo, index=False)
    print(f"[ {datetime.now().strftime('%d/%m/%Y %H:%M:%S')} ] Preco novo gravado em: {xlsx_salvo}")
    
    return df_todos
