#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import pandas as pd
from os import getenv, path
from datetime import datetime
from sqlserver_conn import SQLServerConnection


PASTA_XLS = './xls'
XLS_DESTINO = 'preco_vigente.xlsx'


def pegar_precos_vigentes_bd():
    """Função para pegar os preços vigentes do banco de dados."""

    # Conectar ao banco de dados sql server
    server = getenv('SQLSERVER_HOST')
    database = getenv('SQLSERVER_DATABASE')
    username = getenv('SQLSERVER_USER')
    password = getenv('SQLSERVER_PASSWORD')

    bd = SQLServerConnection(server, database, username, password)
    conn = bd.conectar_bd()
    
    if conn:
        # Fazer SELECT
        df = pd.read_sql(
            """select 
                    a.codemp,
                    a.codtpr cod_tabela_preco,
                    a.codpro cod_produto,
                    cast(a.datger as date) dat_validade_inicial,
                    b.despro str_desc_produto,
                    a.prebas num_preco_base,
                    a.tolmai num_perc_tolerancia_para_mais,
                    a.vltmai num_valor_tolerancia_para_mais
            from E081ITP a
            join e075pro b on a.codpro = b.codpro and a.codemp = b.codemp
            where 
                1 = 1
                and a.codemp = 1
                and a.codtpr = 'ST01'
                and a.prebas > 0
                -- and cast(a.datini as date) = cast(getdate() as date)
                and cast(a.datini as date) = '07/24/2025'
            order by a.codpro""",
            conn
        )
        df.columns = [
            'CodigoEmpresa',
            'TabelaPreco',
            'Codigo',
            'ValidadeInicial',
            'Produtos',
            'R$',
            'PercToleranciaParaMais',
            'ValorToleranciaParaMais',
        ]
        df = df.astype(
            {
                'CodigoEmpresa': int,
                'TabelaPreco': str,
                'Codigo': int,
                'ValidadeInicial': 'datetime64[ns]',
                'Produtos': str,
                'R$': float,
                'PercToleranciaParaMais': float,
                'ValorToleranciaParaMais': float,
            }
        )
        print(df.head())  # Mostra as primeiras linhas da tabela
    bd.fechar_conexao()

    xlsx_salvo = path.join(PASTA_XLS, XLS_DESTINO)
    df.to_excel(xlsx_salvo, index=False)
    print(f"[ {datetime.now().strftime('%d/%m/%Y %H:%M:%S')} ] Preco vigente gravado em: {xlsx_salvo}")

    return df
