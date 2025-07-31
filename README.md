# Diff_Tabela_Precos

Projeto em Python para análise, comparação e exportação de tabelas de preços a partir de arquivos Excel e banco de dados SQL Server.

## Funcionalidades

- Carrega tabelas de preços de arquivos Excel (.xls/.xlsx)
- Conecta ao SQL Server para obter preços vigentes
- Compara tabelas de preços novas e vigentes, identificando diferenças
- Exporta resultados para arquivos Excel
- Filtra, transforma e organiza dados de forma automatizada

## Estrutura do Projeto

```
diff_tabela_precos/
├── src/
│   ├── main.py            # Script principal de execução
│   ├── excel_df.py        # Funções para manipulação de arquivos Excel
│   ├── bd_df.py           # Funções para conexão e consulta ao banco de dados
│   ├── dif_df.py          # Funções para comparação de DataFrames
│   ├── __init__.py        # Variáveis globais e configuração do pacote
├── xls/                   # Pasta para arquivos Excel de entrada e saída
│   ├── Tabela de Preco Representante Geral.xls
│   └── preco_novo.xlsx
├── .env                   # Variáveis de ambiente (dados sensíveis)
├── README.md
```

## Como usar

1. **Instale as dependências:**
   ```sh
   pip install -r requirements.txt
   ```

2. **Configure o arquivo `.env`** com os dados de acesso ao banco SQL Server:
   ```
   SQLSERVER_HOST=seu_servidor
   SQLSERVER_DATABASE=seu_banco
   SQLSERVER_USER=seu_usuario
   SQLSERVER_PASSWORD=sua_senha
   ```

3. **Coloque o arquivo Excel de origem na pasta `xls/`.**

4. **Execute o projeto a partir da raiz:**
   ```sh
   python -m src.main
   ```

## Observações

- Para arquivos `.xls`, é necessário o driver `xlrd`. Para `.xlsx`, utilize `openpyxl`.
- Certifique-se de que o driver ODBC do SQL Server está instalado no sistema.
- As variáveis globais como `PASTA_XLS`, `XLS_ORIGEM` e `XLS_DESTINO` estão em `src/__init__.py`.

## Licença

Este projeto é de uso interno na empresa.