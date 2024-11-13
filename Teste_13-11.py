# Teste: Gerar Dataset

import numpy as np
import csv
import pandas as pd
from datetime import datetime


# Tarefas:
# 1-Leitura e Preparação dos Dados:
# Carregue os dados do arquivo CSV para um array numpy. Cada linha do dataset deve ser representada por um array unidimensional, e o dataset completo deve ser uma matriz 2D.
# Certifique-se de converter as colunas de data, quantidade e preço para tipos apropriados (data como string ou datetime, quantidade e preço como numéricos).

dados = pd.read_csv("vendas.csv")

arrDados = dados.values

# print(arrDados)




# 2-Análise Estatística:
# Calcule a média, mediana e desvio padrão do Valor Total das vendas.

vTotal = []

for i in range(len(arrDados)):
  vTotal.append(arrDados[i][-1])  
np.array(vTotal)

# média:
print(np.mean(vTotal))

# mediana:
print(np.median(vTotal))

# desvio padrão:
print(np.std(vTotal))






# Encontre o produto com a maior quantidade vendida e o produto com o maior valor total de vendas.


produtoA = 0
produtoB = 0
produtoC = 0

for i in range(len(arrDados)):
    if arrDados[i][2] == "Produto A":
        produtoA += arrDados[i][3]
    if arrDados[i][2] == "Produto B":
        produtoB += arrDados[i][3]
    if arrDados[i][2] == "Produto C":
        produtoC += arrDados[i][3]
produtos = [produtoA, produtoB, produtoC]
qVendida = np.array(produtos)

qmVendida = np.amax(qVendida)
vmTotal = np.amax(vTotal)

for i in range(len(produtos)):
    if (qmVendida == produtos[i]) and i == 0:
        print("maior valor total: Produto A")
    if (qmVendida == produtos[i]) and i == 1:
        print("maior valor total: Produto B")
    if (qmVendida == produtos[i]) and i == 2:
        print("maior valor total: Produto C")

for i in range(len(arrDados)):
    if arrDados[i][5] == vmTotal:
        print("maior quantidade vendida: " +arrDados[i][2])




# Calcule o valor total de vendas por região.








# Determine a venda média por dia.
# Análise Temporal:

# Determine o dia da semana com maior número de vendas.
# Calcule a variação diária no valor total de vendas, ou seja, a diferença entre as vendas de um dia e o dia seguinte.
# Desafios Adicionais (Opcional):

# Crie uma função que, dada uma região e um produto, retorne o total de vendas dessa combinação.
# Implemente uma análise de crescimento das vendas ao longo do tempo, ou seja, compare o total de vendas entre dois períodos (ex: janeiro de 2024 e fevereiro de 2024) e calcule o aumento ou diminuição percentual.