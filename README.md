# 🤖 Agentic Data Analyst - E-commerce Intelligence

Um sistema autônomo de Engenharia de Dados e Inteligência Artificial desenvolvido para analisar um volume massivo de dados de e-commerce (~67 milhões de registros) utilizando arquitetura baseada em agentes (ReAct Pattern), processamento in-process (OLAP) e interface interativa.

---

## 📂 Base de Dados Utilizada
O projeto processa o dataset público eCommerce Behavior Data from Multi Category Store (disponibilizado pela REES46 no Kaggle).
- Volume: ~67 milhões de registros de eventos de navegação e consumo.
- Escopo: Dados comportamentais incluindo visualizações de produtos (view), adições ao carrinho (cart) e compras finalizadas (purchase), com preços, marcas e categorias.

---

## 🚀 O Problema & A Solução
Painéis de BI tradicionais são estáticos e limitados a perguntas pré-programadas. Este projeto implementa um Agente Analista Autônomo capaz de receber perguntas de negócio em linguagem natural, inspecionar o esquema do banco de dados, escrever, executar e auto-corrigir consultas SQL em tempo real, gerando relatórios executivos transparentes e lidando com inconsistências do mundo real.

## 🛠️ Stack Tecnológica
- Linguagem: Python
- Orquestração de Agentes: LangChain & LangGraph (ReAct Agent)
- Processamento de Dados (OLAP): DuckDB (alto desempenho in-memory)
- Modelos de IA (LLMs): Google Gemini / Groq (GPT OSS 20B) com suporte a múltiplos provedores (Multi-provider failover)
- Interface Gráfica: Streamlit
- Gerenciamento de Logs: Documentação automatizada em Markdown (.md)

## 📊 Arquitetura e Funcionamento
1. Entrada Natural: O usuário faz uma pergunta complexa de negócio via painel web.
2. Raciocínio Autônomo: O agente investiga as tabelas disponíveis, planeja a estratégia e escreve a query SQL.
3. Execução e Tratamento de Erros: O DuckDB processa os dados em segundos. Se houver falha de sintaxe, o agente lê o erro, se autocorrige e tenta novamente.
4. Governança e Transparência: O sistema entrega a resposta formatada e registra logs detalhados, apontando inclusive inconsistências de governança de dados (como valores nulos em categorias).

## ⚙️ Como Executar o Projeto Localmente

1. Clone o repositório:
   git clone https://github.com/Lcapp29/agent-ai-ecommerce.git
   cd agent-ai-ecommerce

2. Crie e ative o ambiente virtual:
   python -m venv venv
   venv\Scripts\activate

3. Instale as dependências:
   pip install -r requirements.txt

4. Configure suas chaves de API:
   Crie um arquivo .env na raiz e adicione suas credenciais:
   GOOGLE_API_KEY="sua_chave_do_google"
   GROQ_API_KEY="sua_chave_do_groq"

5. Inicie o painel visual:
   streamlit run painel.py