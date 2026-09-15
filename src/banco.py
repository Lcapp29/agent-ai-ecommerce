import duckdb

def conectar_banco():
    """Cria a conexão na memória e carrega o arquivo CSV gigante."""
    # O ':memory:' garante que não vai pesar seu computador, tudo some ao fechar
    conn = duckdb.connect(':memory:')
    
    # Criamos uma "janela" (view) apontando para a pasta dados.
    # Repare no caminho 'dados/2019-Nov.csv'
    conn.execute("""
        CREATE VIEW eventos AS 
        SELECT * FROM read_csv_auto('dados/2019-Nov.csv');
    """)
    
    return conn