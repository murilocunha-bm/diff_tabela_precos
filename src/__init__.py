from os import getenv

PASTA_XLS = './xls'
XLS_TABELA_PRECO = 'Tabela de Preco Representante Geral.xls' 
XLS_PRECO_NOVO = 'preco_novo.xlsx' 
XLS_PRECO_VIGENTE = 'preco_vigente.xlsx' 
XLS_DIFERENCA = 'preco_diferente.xlsx'

SERVER = getenv('SQLSERVER_HOST')
DATABASE = getenv('SQLSERVER_DATABASE')
USERNAME = getenv('SQLSERVER_USER')
PASSWORD = getenv('SQLSERVER_PASSWORD')
