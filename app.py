import os
from datetime import datetime
from dotenv import load_dotenv
from src.agente import criar_agente

# 1. Carrega as senhas do arquivo .env
load_dotenv()

# 2. Inicializa o agente
agente_ecommerce = criar_agente()

# 3. A pergunta de negócios
pergunta = """
Analise os dados de eventos da loja.
Eu preciso saber qual é a marca da categoria de smartphones (electronics.smartphone) 
que tem a maior taxa de abandono de carrinho. Ou seja, a marca que tem muita adição 
ao carrinho ('cart'), mas poucas conversões em compra ('purchase').
Me traga o top 3 com os números absolutos.
"""

print("Iniciando a análise na base de milhões de linhas...")
print("O Agente está raciocinando e criando o SQL...\n")

# Dá o play no agente
resultado = agente_ecommerce.invoke({"messages": [("user", pergunta)]})

# --- A MÁGICA DA LIMPEZA COMEÇA AQUI ---

# Pega o pacote sujo que a IA mandou
resposta_bruta = resultado["messages"][-1].content

# Limpa a sujeira: Se a resposta vier como uma lista cheia de códigos, pegamos só o texto
if isinstance(resposta_bruta, list):
    texto_limpo = resposta_bruta[0].get("text", "Erro ao extrair o texto.")
else:
    # Se já vier limpo, só passamos adiante
    texto_limpo = resposta_bruta

print("--- RESPOSTA FINAL ---")
print(texto_limpo)

# --- SALVANDO O LOG ORGANIZADO ---
data_hora = datetime.now().strftime("%Y%m%d_%H%M%S")
nome_arquivo = f"relatorio_abandono_{data_hora}.md"

# 1. Cria a pasta 'relatorios' se ela ainda não existir
pasta_destino = "relatorios"
os.makedirs(pasta_destino, exist_ok=True)

# 2. Junta o nome da pasta com o nome do arquivo
caminho_completo = os.path.join(pasta_destino, nome_arquivo)

# 3. Salva no lugar certo
with open(caminho_completo, "w", encoding="utf-8") as arquivo_log:
    arquivo_log.write(f"# Pergunta do Diretor\n{pergunta}\n\n")
    arquivo_log.write(f"# Análise da IA\n{texto_limpo}\n")

print(f"\n[SUCESSO] O relatório foi salvo na pasta: {caminho_completo}")