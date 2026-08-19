import pandas as pd
alunos = pd.DataFrame({
 "Nome": [
 "Ana", "Bruno", "Carlos", "Daniela",
 "Eduardo", "Fernanda", "Gabriel", "Helena",
 "Igor", "Julia", "Lucas", "Marina"
 ],
 "Nota": [8, 7, 9, 6, 10, 8, 7, 9, 5, 8, 6, 10]
})

# verifique o tamanho da população
tamanho_populacao = len(alunos)
print(len(alunos))
print(f"Tamanho da população: {tamanho_populacao}")

# Calcule a média da população
media_populacao = alunos['Nota'].mean()
print(f"Média da população: {media_populacao}")

#retire uma amostra aleatória de 5 alunos
amostra = alunos.sample(n=5, random_state=42)
print(f"Amostra aleatória de alunos: {amostra['Nome'].tolist()}")

#calcule a média da amostra
media_amostra = amostra['Nota'].mean()
print(f"Média da amostra: {media_amostra}")

#compare as duas médias e calcule o erro amostral
erro_amostral = abs(media_populacao - media_amostra)
print(f"Erro amostral: {erro_amostral}")

# repita agora com uma amostra de 8 alunos
amostra_8 = alunos.sample(n=8, random_state=42)
print(f"Amostra aleatória de 8 alunos: {amostra_8['Nome'].tolist()}")
media_amostra_8 = amostra_8['Nota'].mean()
print(f"Média da amostra de 8 alunos: {media_amostra_8}")
erro_amostral_8 = abs(media_populacao - media_amostra_8)
print(f"Erro amostral da amostra de 8 alunos: {erro_amostral_8}")
