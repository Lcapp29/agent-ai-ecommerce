from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_groq import ChatGroq
from langgraph.prebuilt import create_react_agent
from src.ferramentas import executar_sql

def criar_agente(provedor="Google"):
    """Monta o agente conectando o raciocínio da IA com as ferramentas."""
    
    # O interruptor lógico: escolhe o motor baseado no que veio da tela
    if provedor == "Groq":
        # Motor super rápido de código aberto
        llm = ChatGroq(model="openai/gpt-oss-20b")
    else:
        # Motor padrão do Google
        llm = ChatGoogleGenerativeAI(model="gemini-3.6-flash")
        
    ferramentas = [executar_sql]
    agente = create_react_agent(llm, ferramentas)
    
    return agente