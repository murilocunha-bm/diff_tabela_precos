#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import pandas as pd
from os import path
from datetime import datetime


PASTA_XLS = './xls'
XLS_DESTINO = 'preco_diferente.xlsx'


def encontrar_diferencas_precos(
        df_antigo:pd.DataFrame,
        df_novo:pd.DataFrame,
        col_ligacao:str,
        col_diferenca:str
    ) -> pd.DataFrame:
    
    df_diferenca_precos = pd.merge(
        df_antigo, 
        df_novo, 
        on=col_ligacao, 
        how='inner', 
        suffixes=('_novo', '_vigente')
    )

    # Filtra apenas onde os valores de R$ são diferentes (considerando NaN)
    df_diferentes = df_diferenca_precos[
        df_diferenca_precos[col_diferenca + '_novo'] != df_diferenca_precos[col_diferenca + '_vigente']
    ]
    # # Para considerar NaN como diferença
    # df_diferentes = df_diferenca_precos[
    #     (df_diferenca_precos['R$_novo'] != df_diferenca_precos['R$_vigente']) |
    #     (df_diferenca_precos['R$_novo'].isna() != df_diferenca_precos['R$_vigente'].isna())
    # ]

    col_desejadas = [
        'Codigo',
        'Produtos_novo',
        'Produtos_vigente',
        'R$_vigente',
        'R$_novo',
    ]
    print(df_diferentes[col_desejadas])
    
    # Seleciona apenas as colunas desejadas do DataFrame original. Copy cria uma cópia independente
    df_resultado = df_diferentes[col_desejadas].copy()

    xlsx_salvo = path.join(PASTA_XLS, XLS_DESTINO)
    df_resultado.to_excel(xlsx_salvo, index=False)
    print(f"[ {datetime.now().strftime('%d/%m/%Y %H:%M:%S')} ] Preco diferente gravado em: {xlsx_salvo}")
