import os
import streamlit as st
from datetime import datetime
from dotenv import load_dotenv
from src.agente import criar_agente

# Carrega as senhas (Google e agora a do Groq)
load_dotenv()

st.set_page_config(page_title="Agente Analista", page_icon="📊")

st.title("🤖 Assistente de Análise de Dados")
st.markdown("Faça perguntas naturais e deixe a IA vasculhar milhões de registros para você.")

# --- O NOVO INTERRUPTOR VISUAL ---
provedor_escolhido = st.radio(
    "Escolha o motor de Inteligência Artificial:",
    ("Google (Gemini)", "Groq (gpt)"),
    horizontal=True
)

# Atualizamos a função de carregar para ela entender qual motor você clicou
@st.cache_resource
def carregar_agente(provedor):
    # Limpa o texto do botão para passar apenas a palavra chave para a função
    nome_provedor = "Groq" if "Groq" in provedor else "Google"
    return criar_agente(provedor=nome_provedor)

# Carrega o agente de acordo com a sua escolha no rádio
agente_ecommerce = carregar_agente(provedor_escolhido)
# ----------------------------------

pergunta = st.text_area(
    "O que você deseja descobrir hoje?", 
    placeholder="Exemplo: Qual é a marca de smartphone com mais abandonos de carrinho?"
)

if st.button("Gerar Análise"):
    if pergunta:
        # Mostra na tela qual motor está trabalhando no momento
        with st.spinner(f"Analisando milhões de linhas usando o motor {provedor_escolhido}..."):
            
            resultado = agente_ecommerce.invoke({"messages": [("user", pergunta)]})
            resposta_bruta = resultado["messages"][-1].content
            
            if isinstance(resposta_bruta, list):
                texto_limpo = resposta_bruta[0].get("text", "Erro ao extrair o texto.")
            else:
                texto_limpo = resposta_bruta
            
            st.success("Análise concluída com sucesso!")
            st.markdown(texto_limpo)

            # Salva o relatório e anota qual motor foi usado
            data_hora = datetime.now().strftime("%Y%m%d_%H%M%S")
            nome_arquivo = f"relatorio_{data_hora}.md"
            pasta_destino = "relatorios"
            
            os.makedirs(pasta_destino, exist_ok=True)
            caminho_completo = os.path.join(pasta_destino, nome_arquivo)
            
            with open(caminho_completo, "w", encoding="utf-8") as arquivo_log:
                arquivo_log.write(f"# Pergunta\n{pergunta}\n\n")
                arquivo_log.write(f"**Motor utilizado:** {provedor_escolhido}\n\n")
                arquivo_log.write(f"# Análise\n{texto_limpo}\n")
                
    else:
        st.warning("Por favor, digite uma pergunta na caixa de texto acima.")