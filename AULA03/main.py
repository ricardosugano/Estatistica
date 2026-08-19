#import random
#alunos = ["Rogério", "Ricardo", "Shimada", "Camila","Alice", "Bob", "Charlie", "David", "Eva", "Kaio", "Ana", "Lucas", "Mariana", "Pedro", "Sofia"]
#from random import random
#random.seed(15)  # Define a semente para reprodutibilidade
#amostra = random.sample(alunos, 3)
#print("Amostra aleatória de alunos:", amostra)

import pandas as pd

df = pd.read_csv("dados.csv")

amostra = df.sample(n=100)  # Seleciona uma amostra aleatória de 10 linhas

print(f"Média da idade: {df['idade'].mean()}")  # Calcula a média da coluna "idade"

print(f"Média da idade na amostra: {amostra['idade'].mean()}")  # Calcula a média da coluna "idade" na amostra

print(f"Erro amostral: {abs(df['idade'].mean() - amostra['idade'].mean())}")  # Calcula o erro amostral