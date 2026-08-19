#import random
#alunos = ["Rogério", "Ricardo", "Shimada", "Camila","Alice", "Bob", "Charlie", "David", "Eva", "Kaio", "Ana", "Lucas", "Mariana", "Pedro", "Sofia"]
#from random import random
#random.seed(15)  # Define a semente para reprodutibilidade
#amostra = random.sample(alunos, 3)
#print("Amostra aleatória de alunos:", amostra)

#import pandas as pd
#df = pd.read_csv("dados.csv")
#amostra = df.sample(n=1000)  # Seleciona uma amostra aleatória de 10 linhas
#print(f"Média da idade: {df['idade'].mean()}")  # Calcula a média da coluna "idade"
#print(f"Média da idade na amostra: {amostra['idade'].mean()}")  # Calcula a média da coluna "idade" na amostra
#print(f"Erro amostral: {abs(df['idade'].mean() - amostra['idade'].mean())}")  # Calcula o erro amostral

import numpy as np
import pandas as pd

np.random.seed(15)  # Define a semente para reprodutibilidade

dados = {"Notas": np.random.normal(70, 10, size=10000)}  # Gera 1000 notas aleatórias com média 50 e desvio padrão 25

df = pd.DataFrame(dados)

amostra = df.sample(n=10000, random_state=15)  # Seleciona uma amostra aleatória de 100 linhas    


media_populacao = df['Notas'].mean()  # Calcula a média da população
media_amostra = amostra['Notas'].mean()  # Calcula a média da amostra

#print(f"Média da população: {media_populacao}")  # Exibe a média da população
#print(f"Média da amostra: {media_amostra}")  # Exibe a média da amostra

for tamanho in [10, 50, 100, 500, 1000]:
    amostra = df.sample(n=tamanho, random_state=15)  # Seleciona uma amostra aleatória de tamanho especificado
    media_amostra = amostra['Notas'].mean()  # Calcula a média da amostra
    erro_amostral = abs(media_populacao - media_amostra)  # Calcula o erro amostral
    print(f"Tamanho da amostra: {tamanho}, Média da amostra: {media_amostra}, Erro amostral: {erro_amostral}")
    
    