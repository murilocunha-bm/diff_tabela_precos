#!.venv/bin/python3
# -*- coding: utf-8 -*-

import pandas as pd

# Substitua 'arquivo.xlsx' pelo nome do seu arquivo
df_original = pd.read_excel(
    './xls/Tabela de Preco Representante Geral.xls', 
    # engine='openpyxl'                 # Use 'openpyxl' para arquivos .xlsx
    engine = 'xlrd',                    # Use 'xlrd' para arquivos .xls
    
)

print(df_original.head(15))                                 # Mostra as primeiras linhas da planilha
df_novo = df_original.drop([                                # Remove as colunas 'Unnamed: 0' e 'Unnamed: 1'
    'Unnamed: 0',
    'Unnamed: 1',
    'Unnamed: 6'
    ],
    axis=1
)    
df_novo = df_novo.dropna(axis=0, how='all')                 # Remove linhas vazias
df_novo = df_novo.iloc[3:]                                  # Remove as três primeiras linhas
df_novo.columns = [                                         # Renomeia as colunas
    'CodigoResfriados',
    'ProdutosResfriadosTraseiro',
    'PesoCaixaResfriados',
    'R$Resfriados',
    'CodigoOrigem',
    'LinhaOrigem',
    'PesoCaixaOrigem',
    'R$Origem',
]
for col in ['PesoCaixaResfriados', 'PesoCaixaOrigem']:
    df_novo.loc[df_novo.index[0:], col ] = (
        df_novo.loc[df_novo.index[0:], col ]
        .astype(str)
        .str.replace('kg', '', regex=False)
        .str.strip()
    )
df_novo = df_novo.astype(
    {
        'CodigoResfriados': str,
        'ProdutosResfriadosTraseiro': str,
        'PesoCaixaResfriados': float,
        'R$Resfriados': float,
        'CodigoOrigem': str,
        'LinhaOrigem': str,
        'PesoCaixaOrigem': float,
        'R$Origem': float,
    }
)
print(df_novo.head(15))                                     # Mostra as primeiras linhas da planilha





# print(df_original.info())  # Mostra as primeiras linhas da planilha