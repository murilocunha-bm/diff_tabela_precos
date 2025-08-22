#!.venv/bin/python3
# -*- coding: utf-8 -*-


from datetime import datetime
from pyodbc import connect
from sqlalchemy import create_engine


class SQLServerConnection():
    # String de conexão
    def __init__(self, server, database, username, password):
        self.server = server
        self.database = database
        self.username = username
        self.password = password
        self.odbc_str = f'DRIVER={{ODBC Driver 17 for SQL Server}};'
        self.sqlalchemy_str = f'mssql+pyodbc:///?odbc_connect={self.odbc_str}'
        self.login_str = f'SERVER={self.server};DATABASE={self.database};UID={self.username};PWD={self.password}'
        self.conn = None


    def conectar_odbc(self):
        """Função para conectar ao banco de dados SQL Server."""
        try:
            conn_str = self.odbc_str + self.login_str
            self.conn = connect(conn_str)
            print(f"[ {datetime.now().strftime('%d/%m/%Y %H:%M:%S')} ] Conexão ODBC bem-sucedida!")
            return self.conn
        except Exception as e:
            print(f"[ {datetime.now().strftime('%d/%m/%Y %H:%M:%S')} - ERRO ] ODBC sem conexão: {e}")
            return None


    def conectar_sqlalchemy(self):
        """Função para conectar ao banco de dados SQL Server."""
        try:
            conn_str = self.sqlalchemy_str + self.login_str
            sqlalchemy_engine = create_engine(conn_str)
            self.conn = sqlalchemy_engine.connect()
            print(f"[ {datetime.now().strftime('%d/%m/%Y %H:%M:%S')} ] Conexão SQLAlchemy bem-sucedida!")
            return self.conn
        except Exception as e:
            print(f"[ {datetime.now().strftime('%d/%m/%Y %H:%M:%S')} - ERRO ] SQLAlchemy sem conexão: {e}")
            return None


    def fechar_conexao(self):
        """Função para fechar a conexão com o banco de dados."""
        if self.conn:
            self.conn.close()
            print(f"[ {datetime.now().strftime('%d/%m/%Y %H:%M:%S')} ] Conexão fechada.")
        else:
            print(f"[ {datetime.now().strftime('%d/%m/%Y %H:%M:%S')} ] Nenhuma conexão para fechar.")


