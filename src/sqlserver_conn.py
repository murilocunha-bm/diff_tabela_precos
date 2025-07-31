#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import pyodbc
from datetime import datetime


class SQLServerConnection():
    # String de conexão
    def __init__(self, server, database, username, password):

        self.server = server
        self.database = database
        self.username = username
        self.password = password
        self.conn_str = (
            f"DRIVER={{ODBC Driver 17 for SQL Server}};"
            f"SERVER={server};DATABASE={database};UID={username};PWD={password}"
        )
        self.conn = None
        
        
    def conectar_bd(self):
        """Função para conectar ao banco de dados SQL Server."""
        try:
            self.conn = pyodbc.connect(self.conn_str)
            print(f"[ {datetime.now().strftime('%d/%m/%Y %H:%M:%S')} ] Conexão bem-sucedida!")
            return self.conn
        
        except Exception as e:
            print(f"[ {datetime.now().strftime('%d/%m/%Y %H:%M:%S')} ] Erro ao conectar: {e}")
            return None


    def fechar_conexao(self):
        """Função para fechar a conexão com o banco de dados."""
        if self.conn:
            self.conn.close()
            print(f"[ {datetime.now().strftime('%d/%m/%Y %H:%M:%S')} ] Conexão fechada.")
        else:
            print(f"[ {datetime.now().strftime('%d/%m/%Y %H:%M:%S')} ] Nenhuma conexão para fechar.")


