#!.venv/bin/python3
# -*- coding: utf-8 -*-


#
# Importando as variáveis de ambiente. Deve vir antes de qualquer importação que dependa delas.
from dotenv import load_dotenv
load_dotenv() 
#
from datetime import datetime
from os import remove, path
#
from src.excel_df import montar_tabela_unica, criar_csv_custos
from src.bd_df import pegar_precos_vigentes_bd
from src.dif_df import encontrar_diferencas_precos
from src import SQL_TB_ST01, SQL_TB_SP02, SQL_TB_SP03
from src import MAPA_TABELA_PRECO_NOVO_ST, MAPA_TABELA_PRECO_NOVO_SP2, MAPA_TABELA_PRECO_NOVO_SP3, MAPA_TABELA_CUSTOS_SP
from src import XLS_PRECO_NOVO_ST, XLS_PRECO_NOVO_SP2, XLS_PRECO_NOVO_SP3
from src import XLS_PRECO_VIGENTE_ST, XLS_PRECO_VIGENTE_SP2, XLS_PRECO_VIGENTE_SP3
from src import XLS_DIFERENCA_ST, XLS_DIFERENCA_SP2, XLS_DIFERENCA_SP3
from src import CSV_CUSTOS


def apagar_arquivos_criados_antes():
    arquivos_criados = [
        XLS_PRECO_NOVO_ST, XLS_PRECO_NOVO_SP2, XLS_PRECO_NOVO_SP3,
        XLS_PRECO_VIGENTE_ST, XLS_PRECO_VIGENTE_SP2, XLS_PRECO_VIGENTE_SP3,
        XLS_DIFERENCA_ST, XLS_DIFERENCA_SP2, XLS_DIFERENCA_SP3,
        CSV_CUSTOS,
    ]
    for arquivo in arquivos_criados:
        if path.isfile(arquivo):
            remove(arquivo)
            print(f"[ {datetime.now().strftime('%d/%m/%Y %H:%M:%S')} ] Arquivo {arquivo} excluído com sucesso.")
        else:
            print(f"[ {datetime.now().strftime('%d/%m/%Y %H:%M:%S')} ] Arquivo {arquivo} não encontrado.")


def encontrar_diferencas_tabelas_precos():
    etapas = (
        (MAPA_TABELA_PRECO_NOVO_ST, XLS_PRECO_NOVO_ST, SQL_TB_ST01, XLS_PRECO_VIGENTE_ST, XLS_DIFERENCA_ST,),
        (MAPA_TABELA_PRECO_NOVO_SP2, XLS_PRECO_NOVO_SP2, SQL_TB_SP02, XLS_PRECO_VIGENTE_SP2, XLS_DIFERENCA_SP2,),
        # (MAPA_TABELA_PRECO_NOVO_SP3, XLS_PRECO_NOVO_SP3, SQL_TB_SP03, XLS_PRECO_VIGENTE_SP3, XLS_DIFERENCA_SP3,),
    )

    for etapa in etapas:

        print(f"[ {datetime.now().strftime('%d/%m/%Y %H:%M:%S')} ] Tabela de precos: {etapa[0][0]['nome_xlsx']}...")

        df_precos_novos = montar_tabela_unica(
            lst_preco_novo=etapa[0],
            nome_xlsx_destino=etapa[1],
        )

        if not df_precos_novos.empty:
            df_precos_vigentes = pegar_precos_vigentes_bd(
                sql_tabela_precos=etapa[2], 
                nome_xlsx_destino=etapa[3]
            )
            
            if not df_precos_vigentes.empty:
                encontrar_diferencas_precos(
                    nome_xlsx_diferenca=etapa[4],
                    df_antigo=df_precos_novos,
                    df_novo=df_precos_vigentes,
                    col_ligacao='Codigo',
                    col_diferenca='R$'
                )
        else:
            print(f"[ {datetime.now().strftime('%d/%m/%Y %H:%M:%S')} - ERRO ] Tabela de preços novos vazia. Verifique os dados.")


if __name__ == "__main__":
    print(f"[ {datetime.now().strftime('%d/%m/%Y %H:%M:%S')} ] Iniciando sistema")
    
    print(f"[ {datetime.now().strftime('%d/%m/%Y %H:%M:%S')} ] Apagando arquivos de resultado criados antes...")
    apagar_arquivos_criados_antes()

    print(f"[ {datetime.now().strftime('%d/%m/%Y %H:%M:%S')} ] Iniciando o processamento da tabela de preços...")
    encontrar_diferencas_tabelas_precos()

    print(f"[ {datetime.now().strftime('%d/%m/%Y %H:%M:%S')} ] Iniciando criação de csv de custos para sp...")
    criar_csv_custos(mapa_custos=MAPA_TABELA_CUSTOS_SP, csv_filename=CSV_CUSTOS)

    print(f"[ {datetime.now().strftime('%d/%m/%Y %H:%M:%S')} ] Processamento concluído.")
