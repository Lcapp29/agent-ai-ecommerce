from langchain_core.tools import tool
from src.banco import conectar_banco

# Ligamos o banco de dados uma única vez para a ferramenta usar
conexao = conectar_banco()

@tool
def executar_sql(consulta_sql: str) -> str:
    """
    Executa comandos SQL na tabela 'eventos'.
    
    Regras da tabela 'eventos':
    - event_time: data e hora do evento
    - event_type: o que o cliente fez ('view' para visualizou, 'cart' para adicionou ao carrinho, 'purchase' para comprou)
    - product_id: código único do produto
    - category_code: tipo do produto (exemplo: electronics.smartphone)
    - brand: marca do produto (exemplo: apple, samsung)
    - price: preço do produto em dólares
    - user_id: código de identificação do cliente
    - user_session: código da visita do cliente no site
    """
    try:
        # Pega a consulta da IA, roda no banco e transforma numa tabela legível
        resultado = conexao.execute(consulta_sql).fetchdf()
        return resultado.to_string()
    except Exception as erro:
        # O mecanismo de auto-correção: a IA lê o erro e tenta consertar
        return f"Erro no SQL. Leia o erro, corrija o código e tente novamente: {erro}"