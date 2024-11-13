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
print()


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
        print("maior quantidade vendida: " + arrDados[i][2] + "\n")


# Calcule o valor total de vendas por região.
vTotalN = 0
vTotalS = 0
vTotalL = 0
vTotalO = 0

for i in range(len(arrDados)):
    if arrDados[i][1] == "Norte":
        vTotalN += arrDados[i][-1]
    if arrDados[i][1] == "Sul":
        vTotalS += arrDados[i][-1]
    if arrDados[i][1] == "Leste":
        vTotalL += arrDados[i][-1]
    if arrDados[i][1] == "Oeste":
        vTotalO += arrDados[i][-1]

print("Norte: %.2f\nSul: %.2f\nLeste: %.2f\nOeste: %.2f\n" %
(vTotalN, vTotalS, vTotalL, vTotalO))


# Determine a venda média por dia.
def converter_data(data_str): 
    return datetime.strptime(data_str, "%Y-%m-%d") 

datas = np.array([converter_data(data) for data in arrDados[:, 0]])
indices_ordenados = np.argsort(datas)
datas_ordenadas = arrDados[indices_ordenados]

data_inicial = converter_data(datas_ordenadas[0][0])
data_final = converter_data(datas_ordenadas[-1][0])
diasPassados = (data_final - data_inicial).days + 1

qVendida = 0
for i in range(len(arrDados)):
    qVendida += arrDados[i][3]

print("venda média por dia: %.4f \n" % (qmVendida/diasPassados))


# 3-Análise Temporal:

# Determine o dia da semana com maior número de vendas.

dados = pd.DataFrame(arrDados, columns=['Data', 'Produto', 'Quantidade', 'ValorUnitario', 'Regiao', 'ValorTotal'])
dados['Data'] = pd.to_datetime(dados['Data'])
vendas_por_dia_da_semana = dados['Data'].dt.day_name().value_counts()
dia_com_mais_vendas = vendas_por_dia_da_semana.idxmax()
print(f'Dia da semana com maior número de vendas: {dia_com_mais_vendas}\n')


# Calcule a variação diária no valor total de vendas, ou seja, a diferença entre as vendas de um dia e o dia seguinte.
pd.set_option('future.no_silent_downcasting', True)
vendas_por_dia = dados.groupby('Data')['ValorTotal'].sum()
variacao_diaria_vendas = vendas_por_dia.diff().fillna(0).infer_objects(copy=False)
print('Variação diária no valor total das vendas:')
print(variacao_diaria_vendas)