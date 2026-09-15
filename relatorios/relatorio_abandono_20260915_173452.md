# Pergunta do Diretor

Analise os dados de eventos da loja.
Eu preciso saber qual é a marca da categoria de smartphones (electronics.smartphone) 
que tem a maior taxa de abandono de carrinho. Ou seja, a marca que tem muita adição 
ao carrinho ('cart'), mas poucas conversões em compra ('purchase').
Me traga o top 3 com os números absolutos.


# Análise da IA
Para responder à sua análise na categoria **`electronics.smartphone`**, calculamos o total de adições ao carrinho (`cart`), o total de compras (`purchase`), a quantidade de carrinhos abandonados (`carrinhos - compras`) e a **taxa de abandono** ($\frac{\text{Carrinhos} - \text{Compras}}{\text{Carrinhos}} \times 100$).

---

### 1. Top 3 Marcas por Maior Taxa de Abandono (%) 
*(Considerando marcas com volume expressivo de adições ao carrinho, ou seja, mais de 1.000 adições)*

| Posição | Marca | Adições ao Carrinho (`cart`) | Compras Realizadas (`purchase`) | Carrinhos Abandonados (Absoluto) | Taxa de Abandono (%) |
| :---: | :--- | :---: | :---: | :---: | :---: |
| **1º** | **OnePlus** | 2.269 | 545 | **1.724** | **75,98%** |
| **2º** | **Xiaomi** | 188.847 | 48.553 | **140.294** | **74,29%** |
| **3º** | **Nokia** | 2.301 | 654 | **1.647** | **71,58%** |

> **Destaque:** A **Xiaomi** destaca-se negativamente por ter um volume altíssimo de interação (mais de 188 mil adições ao carrinho) aliado a uma das maiores taxas de abandono da categoria (**74,29%**).

---

### 2. Top 3 Marcas por Volume Absoluto de Carrinhos Abandonados
*(Marcas com o maior número total bruto de desistências de compra)*

| Posição | Marca | Adições ao Carrinho (`cart`) | Compras Realizadas (`purchase`) | Carrinhos Abandonados (Absoluto) | Taxa de Abandono (%) |
| :---: | :--- | :---: | :---: | :---: | :---: |
| **1º** | **Samsung** | 462.102 | 161.791 | **300.311** | **64,99%** |
| **2º** | **Apple** | 372.077 | 127.252 | **244.825** | **65,80%** |
| **3º** | **Xiaomi** | 188.847 | 48.553 | **140.294** | **74,29%** |

---

### Observação Geral
- Marcas com baixíssimo volume de interação (ex: *Micromax* com 10 carrinhos e 0 compras, ou *Vertex* com 2 carrinhos e 0 compras) possuem 100% de taxa teórica de abandono, mas não possuem representatividade de volume ("muita adição ao carrinho").
