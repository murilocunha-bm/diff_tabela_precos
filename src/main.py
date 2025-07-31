#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from os import path
from datetime import datetime
from dotenv import load_dotenv
#
from excel_df import montar_tabela_unica
from bd_df import pegar_precos_vigentes_bd
from dif_df import encontrar_diferencas_precos


def main():
    print(f"[ {datetime.now().strftime('%d/%m/%Y %H:%M:%S')} ] Montando tabela unica de precos...")
    df_precos_novos = montar_tabela_unica()
    print(f"[ {datetime.now().strftime('%d/%m/%Y %H:%M:%S')} ] Concluído tabela unica de precos novos.")

    print(f"[ {datetime.now().strftime('%d/%m/%Y %H:%M:%S')} ] Montando tabela precos vigentes...")
    df_precos_vigentes = pegar_precos_vigentes_bd()
    print(f"[ {datetime.now().strftime('%d/%m/%Y %H:%M:%S')} ] Concluído tabela de precos vigentes.")
    
    print(f"[ {datetime.now().strftime('%d/%m/%Y %H:%M:%S')} ] Procurando diferencas...")
    encontrar_diferencas_precos(
        df_precos_novos,
        df_precos_vigentes,
        col_ligacao='Codigo',
        col_diferenca='R$'
    )
    print(f"[ {datetime.now().strftime('%d/%m/%Y %H:%M:%S')} ] Diferencas gravadas com sucesso.")


if __name__ == "__main__":
    print(f"[ {datetime.now().strftime('%d/%m/%Y %H:%M:%S')} ] Iniciando o processamento da tabela de preços...")
        
    load_dotenv()
    
    main()

    print(f"[ {datetime.now().strftime('%d/%m/%Y %H:%M:%S')} ] Processamento concluído.")
