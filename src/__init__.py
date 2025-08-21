from os import getenv, path


PASTA_XLS = './xls'
XLS_TABELA_PRECO_ST = path.join(PASTA_XLS, 'Tabela de Preco Representante Geral.xls') 
XLS_TABELA_PRECO_SP = path.join(PASTA_XLS, 'Tabela Barra Mansa 21-08-2025.xlsx')
XLS_TABELA_CUSTOS = path.join(PASTA_XLS, 'Tabela Barra Mansa 21-08-2025.xlsx')
CSV_CUSTOS = path.join(PASTA_XLS, 'custos.csv')
# XLS_TABELA_PRECO_SP = path.join(PASTA_XLS, 'Tabela Barra Mansa 15-08-2025.xlsx')
XLS_PRECO_NOVO_ST = path.join(PASTA_XLS, 'preco_novo_st.xlsx')
XLS_PRECO_NOVO_SP2 = path.join(PASTA_XLS, 'preco_novo_sp2.xlsx')
XLS_PRECO_NOVO_SP3 = path.join(PASTA_XLS, 'preco_novo_sp3.xlsx')
XLS_PRECO_VIGENTE_ST = path.join(PASTA_XLS, 'preco_vigente_st.xlsx')
XLS_PRECO_VIGENTE_SP2 = path.join(PASTA_XLS, 'preco_vigente_sp2.xlsx')
XLS_PRECO_VIGENTE_SP3 = path.join(PASTA_XLS, 'preco_vigente_sp3.xlsx')
XLS_DIFERENCA_ST = path.join(PASTA_XLS, 'preco_diferente_st.xlsx')
XLS_DIFERENCA_SP2 = path.join(PASTA_XLS, 'preco_diferente_sp2.xlsx')
XLS_DIFERENCA_SP3 = path.join(PASTA_XLS, 'preco_diferente_sp3.xlsx')

SERVER = getenv('SQLSERVER_HOST')
DATABASE = getenv('SQLSERVER_DATABASE')
USERNAME = getenv('SQLSERVER_USER')
PASSWORD = getenv('SQLSERVER_PASSWORD')

# Tabela de precos de Sertaozinho
SQL_TB_ST01 = """
select 
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
	and b.sitpro = 'A'
    and a.codemp = 1
    and a.codtpr = 'ST01'
    and a.prebas > 0
    and cast(a.datini as date) = (
        select cast(max(x.datini) as date)
        from e081itp x
        where
            1 = 1
            and x.codemp = a.codemp
            and x.codtpr = a.codtpr
            and x.prebas > 0
    )
    /* and cast(a.datini as date) = '07/24/2025' */
order by a.codpro"""

MAPA_TABELA_PRECO_NOVO_ST = [
    {
        'nome_xlsx': XLS_TABELA_PRECO_ST,
        'nome_sheet': 'Tabela Base',
        'nome_colunas': ['Codigo', 'Produtos', 'PesoCaixa', 'R$', 'Qtde'],  # colocar as colunas a apagar como: del01, del02, del03...
        'linhas_pular': 5,                                                  # inicia em ZERO
        'colunas_ler': 'C:G',
        'linhas_ler': 46
    },
    {
        'nome_xlsx': XLS_TABELA_PRECO_ST,
        'nome_sheet': 'Tabela Base',
        'nome_colunas': ['Codigo', 'Produtos', 'PesoCaixa', 'R$', 'Qtde'],  # colocar as colunas a apagar como: del01, del02, del03...
        'linhas_pular': 53,                                                 # inicia em ZERO
        'colunas_ler': 'C:G',
        'linhas_ler': 10
    },
    {
        'nome_xlsx': XLS_TABELA_PRECO_ST,
        'nome_sheet': 'Tabela Base',
        'nome_colunas': ['Codigo', 'Produtos', 'PesoCaixa', 'R$', 'Qtde'],  # colocar as colunas a apagar como: del01, del02, del03...
        'linhas_pular': 65,                                                 # inicia em ZERO
        'colunas_ler': 'C:G',
        'linhas_ler': 4
    },
    {
        'nome_xlsx': XLS_TABELA_PRECO_ST,
        'nome_sheet': 'Tabela Base',
        'nome_colunas': ['Codigo', 'Produtos', 'PesoCaixa', 'R$', 'Qtde'],  # colocar as colunas a apagar como: del01, del02, del03...
        'linhas_pular': 5,                                          # inicia em ZERO
        'colunas_ler': 'H:K',                                       # coluna K nao existe na planilha (os dados terminam antes, entao, o excel ignora as outras colunas)
        'linhas_ler': 6
    },
    {
        'nome_xlsx': XLS_TABELA_PRECO_ST,
        'nome_sheet': 'Tabela Base',
        'nome_colunas': ['Codigo', 'Produtos', 'PesoCaixa', 'R$', 'Qtde'],  # colocar as colunas a apagar como: del01, del02, del03...
        'linhas_pular': 13,                                         # inicia em ZERO
        'colunas_ler': 'H:K',                                       # coluna K nao existe na planilha (os dados terminam antes, entao, o excel ignora as outras colunas)
        'linhas_ler': 6
    },
    {
        'nome_xlsx': XLS_TABELA_PRECO_ST,
        'nome_sheet': 'Tabela Base',
        'nome_colunas': ['Codigo', 'Produtos', 'PesoCaixa', 'R$', 'Qtde'],  # colocar as colunas a apagar como: del01, del02, del03...
        'linhas_pular': 21,                                         # inicia em ZERO
        'colunas_ler': 'H:K',                                       # coluna K nao existe na planilha (os dados terminam antes, entao, o excel ignora as outras colunas)
        'linhas_ler': 17
    },
    {
        'nome_xlsx': XLS_TABELA_PRECO_ST,
        'nome_sheet': 'Tabela Base',
        'nome_colunas': ['Codigo', 'Produtos', 'PesoCaixa', 'R$', 'Qtde'],  # colocar as colunas a apagar como: del01, del02, del03...
        'linhas_pular': 40,                                         # inicia em ZERO
        'colunas_ler': 'H:K',                                       # coluna K nao existe na planilha (os dados terminam antes, entao, o excel ignora as outras colunas)
        'linhas_ler': 3
    },
    {
        'nome_xlsx': XLS_TABELA_PRECO_ST,
        'nome_sheet': 'Tabela Base',
        'nome_colunas': ['Codigo', 'Produtos', 'PesoCaixa', 'R$', 'Qtde'],  # colocar as colunas a apagar como: del01, del02, del03...
        'linhas_pular': 45,                                         # inicia em ZERO
        'colunas_ler': 'H:K',                                       # coluna K nao existe na planilha (os dados terminam antes, entao, o excel ignora as outras colunas)
        'linhas_ler': 6
    },
    {
        'nome_xlsx': XLS_TABELA_PRECO_ST,
        'nome_sheet': 'Tabela Base',
        'nome_colunas': ['Codigo', 'Produtos', 'PesoCaixa', 'R$', 'Qtde'],  # colocar as colunas a apagar como: del01, del02, del03...
        'linhas_pular': 53,                                         # inicia em ZERO
        'colunas_ler': 'H:K',                                       # coluna K nao existe na planilha (os dados terminam antes, entao, o excel ignora as outras colunas)
        'linhas_ler': 6
    },
    {
        'nome_xlsx': XLS_TABELA_PRECO_ST,
        'nome_sheet': 'Tabela Base',
        'nome_colunas': ['Codigo', 'Produtos', 'PesoCaixa', 'R$', 'Qtde'],  # colocar as colunas a apagar como: del01, del02, del03...
        'linhas_pular': 61,                                         # inicia em ZERO
        'colunas_ler': 'H:K',                                       # coluna K nao existe na planilha (os dados terminam antes, entao, o excel ignora as outras colunas)
        'linhas_ler': 3
    },
    {
        'nome_xlsx': XLS_TABELA_PRECO_ST,
        'nome_sheet': 'Tabela Base',
        'nome_colunas': ['Codigo', 'Produtos', 'PesoCaixa', 'R$', 'Qtde'],  # colocar as colunas a apagar como: del01, del02, del03...
        'linhas_pular': 66,                                         # inicia em ZERO
        'colunas_ler': 'H:K',                                       # coluna K nao existe na planilha (os dados terminam antes, entao, o excel ignora as outras colunas)
        'linhas_ler': 4
    }
]

MAPA_TABELA_PRECO_NOVO_SP2 = [
    {
        'nome_xlsx': XLS_TABELA_PRECO_SP,
        'nome_sheet': 'Tabela Base',
        'nome_colunas': ['Codigo', 'Produtos', 'PesoCaixa', 'R$', 'del01', 'del02', 'Qtde'],  # colocar as colunas a apagar como: del01, del02, del03...
        'linhas_pular': 11,                                         # inicia em ZERO
        'colunas_ler': 'B:H',
        'linhas_ler': 300
    },
]

# Tabela de precos de SP
SQL_TB_SP02 = """
select 
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
	and b.sitpro = 'A'
    and a.codemp = 1
    and a.codtpr = 'SP02'
    and a.prebas > 0
    and cast(a.datini as date) = (
        select cast(max(x.datini) as date)
        from e081itp x
        where
            1 = 1
            and x.codemp = a.codemp
            and x.codtpr = a.codtpr
            and x.prebas > 0
    )
    /* and cast(a.datini as date) = '07/24/2025' */
order by a.codpro"""


MAPA_TABELA_PRECO_NOVO_SP3 = [
    {
        'nome_xlsx': XLS_TABELA_PRECO_SP,
        'nome_sheet': 'Tabela Base',
        'nome_colunas': ['Codigo', 'Produtos', 'PesoCaixa', 'del01', 'R$', 'del01', 'Qtde'],    # colocar as colunas a apagar como: del01, del02, del03...
        'linhas_pular': 11,                                                                     # inicia em ZERO
        'colunas_ler': 'B:H',
        'linhas_ler': 300
    },
]

# Tabela de precos de SP
SQL_TB_SP03 = """
select 
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
	and b.sitpro = 'A'
    and a.codemp = 1
    and a.codtpr = 'SP03'
    and a.prebas > 0
    and cast(a.datini as date) = (
        select cast(max(x.datini) as date)
        from e081itp x
        where
            1 = 1
            and x.codemp = a.codemp
            and x.codtpr = a.codtpr
            and x.prebas > 0
    )
    /* and cast(a.datini as date) = '07/24/2025' */
order by a.codpro"""


MAPA_TABELA_CUSTOS_SP = [
    {
        'nome_xlsx': XLS_TABELA_CUSTOS,
        'nome_sheet': 'Tabela Base',
        'nome_colunas': ['Codigo', 'del01', 'del02', 'del03', 'del04', 'del05', 'del06', 'del07', 'del08', 'Custo'],
        'linhas_pular': 11,
        'colunas_ler': 'B:K',
        'linhas_ler': 300
    },

]