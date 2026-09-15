# Pergunta do Diretor

Analise os dados de eventos da loja.
Eu preciso saber qual é a marca da categoria de smartphones (electronics.smartphone) 
que tem a maior taxa de abandono de carrinho. Ou seja, a marca que tem muita adição 
ao carrinho ('cart'), mas poucas conversões em compra ('purchase').
Me traga o top 3 com os números absolutos.


# Análise da IA
Para analisar a taxa de abandono de carrinho na categoria de smartphones (`electronics.smartphone`), calculamos a relação entre os eventos de adição ao carrinho (`cart`) e os eventos de conversão em compra (`purchase`):

$$\text{Taxa de Abandono (\%)} = \left( 1 - \frac{\text{Compras}}{\text{Carrinhos}} \right) \times 100 = \frac{\text{Carrinhos} - \text{Compras}}{\text{Carrinhos}} \times 100$$

---

### 1. Top 3 por Maior Taxa de Abandono (%) *(Marcas com Volume Expressivo)*

Considerando as marcas com volume relevante de interações no site (acima de 1.000 adições ao carrinho):

1. **OnePlus**: **75,98%** de taxa de abandono  
   - **Adições ao Carrinho (`cart`):** 2.269  
   - **Compras (`purchase`):** 545  
   - **Carrinhos Abandonados (absoluto):** **1.724**

2. **Xiaomi**: **74,29%** de taxa de abandono  
   - **Adições ao Carrinho (`cart`):** 188.847  
   - **Compras (`purchase`):** 48.553  
   - **Carrinhos Abandonados (absoluto):** **140.294**

3. **Nokia**: **71,58%** de taxa de abandono  
   - **Adições ao Carrinho (`cart`):** 2.301  
   - **Compras (`purchase`):** 654  
   - **Carrinhos Abandonados (absoluto):** **1.647**

> 📌 **Destaque:** A **Xiaomi** é o caso crítico da loja, pois possui um volume massivo de interesse (quase 189 mil carrinhos), mas perde cerca de 3 em cada 4 vendas intencionadas.

---

### 2. Top 3 por Volume Absoluto de Carrinhos Abandonados

Se analisarmos estritamente pelo número de carrinhos que não viraram compra (volume absoluto de vendas perdidas):

1. **Samsung**: **300.311** carrinhos abandonados (Taxa de abandono: **64,99%**)  
   - *Carrinhos:* 462.102 | *Compras:* 161.791
2. **Apple**: **244.825** carrinhos abandonados (Taxa de abandono: **65,80%**)  
   - *Carrinhos:* 372.077 | *Compras:* 127.252
3. **Xiaomi**: **140.294** carrinhos abandonados (Taxa de abandono: **74,29%**)  
   - *Carrinhos:* 188.847 | *Compras:* 48.553

---

### Visão Geral das Principais Marcas de Smartphone

| Marca | Adições ao Carrinho (`cart`) | Compras (`purchase`) | Carrinhos Abandonados | Taxa de Abandono (%) |
| :--- | :---: | :---: | :---: | :---: |
| **OnePlus** | 2.269 | 545 | **1.724** | **75,98%** |
| **Xiaomi** | 188.847 | 48.553 | **140.294** | **74,29%** |
| **Nokia** | 2.301 | 654 | **1.647** | **71,58%** |
| **Huawei** | 67.114 | 21.636 | **45.478** | **67,76%** |
| **Vivo** | 5.911 | 1.914 | **3.997** | **67,62%** |
| **Sony** | 1.410 | 458 | **952** | **67,52%** |
| **Honor** | 2.082 | 699 | **1.383** | **66,43%** |
| **Oppo** | 44.627 | 15.080 | **29.547** | **66,21%** |
| **Apple** | 372.077 | 127.252 | **244.825** | **65,80%** |
| **Samsung** | 462.102 | 161.791 | **300.311** | **64,99%** |
