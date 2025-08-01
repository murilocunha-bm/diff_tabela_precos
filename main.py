#!.venv/bin/python3
# -*- coding: utf-8 -*-


from os import path
from datetime import datetime
from dotenv import load_dotenv
#
from src.excel_df import montar_tabela_unica
from src.bd_df import pegar_precos_vigentes_bd
from src.dif_df import encontrar_diferencas_precos


def main():
    print(f"[ {datetime.now().strftime('%d/%m/%Y %H:%M:%S')} ] Montando tabela unica de precos...")
    df_precos_novos = montar_tabela_unica()
    print(f"[ {datetime.now().strftime('%d/%m/%Y %H:%M:%S')} ] Concluído tabela unica de precos novos.")

    print(f"[ {datetime.now().strftime('%d/%m/%Y %H:%M:%S')} ] Montando tabela precos vigentes...")
    df_precos_vigentes = pegar_precos_vigentes_bd()
    print(f"[ {datetime.now().strftime('%d/%m/%Y %H:%M:%S')} ] Concluído tabela de precos vigentes.")
    
    if not df_precos_novos.empty and not df_precos_vigentes.empty:
        print(f"[ {datetime.now().strftime('%d/%m/%Y %H:%M:%S')} ] Procurando diferencas...")
        encontrar_diferencas_precos(
            df_precos_novos,
            df_precos_vigentes,
            col_ligacao='Codigo',
            col_diferenca='R$'
        )
        print(f"[ {datetime.now().strftime('%d/%m/%Y %H:%M:%S')} ] Diferencas gravadas com sucesso.")
    else:
        print(f"[ {datetime.now().strftime('%d/%m/%Y %H:%M:%S')} - ERRO ] Não foi possível encontrar as tabelas de preços. Verifique os dados.")

if __name__ == "__main__":
    print(f"[ {datetime.now().strftime('%d/%m/%Y %H:%M:%S')} ] Iniciando o processamento da tabela de preços...")
        
    load_dotenv()
    
    main()

    print(f"[ {datetime.now().strftime('%d/%m/%Y %H:%M:%S')} ] Processamento concluído.")
