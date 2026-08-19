# crie um dataframe com 30 alunos com nome, idade e nota

import pandas as pd
alunos = pd.DataFrame({
    "Nome": [
        "Ana", "Bruno", "Carlos", "Daniela", "Eduardo", "Fernanda", "Gabriel", "Helena", "Igor", "Julia",
        "Lucas", "Marina", "Nicolas", "Olivia", "Pedro", "Quintino", "Rafael", "Sofia", "Thiago", "Valentina",
        "William", "Ximena", "Yago", "Zoe", "Adriano", "Bianca", "Cecília", "Davi", "Eloisa", "Felipe"
    ],
    "Idade": [
        20, 21, 19, 22, 20, 21, 19, 22, 20, 21,
        19, 22, 20, 21, 19, 22, 20, 21, 19, 22,
        20, 21, 19, 22, 20, 21, 19, 22, 20, 21
    ],
    "Nota": [
        8.5, 7.5, 9.0, 6.5, 10.0, 8.0, 7.5, 9.0, 5.5, 8.0,  
        6.0, 10.0, 7.5, 8.5, 9.0, 6.5, 10.0, 8.0, 7.5, 9.0,
        5.5, 8.0, 6.0, 10.0, 7.5, 8.5, 9.0, 6.5, 10.0, 8.0
    ]
})

# Calcule a média da população para idade e nota
media_idade_populacao = alunos['Idade'].mean()
media_nota_populacao = alunos['Nota'].mean()
print(f"Média da idade da população: {media_idade_populacao}")
print(f"Média da nota da população: {media_nota_populacao}")

# selecione uma amostra aleatória de 5 alunos
amostra = alunos.sample(n=5)
print("Amostra aleatória de 5 alunos:")
print(amostra)

# Calcule a média da amostra para idade e nota
media_idade_amostra = amostra['Idade'].mean()
media_nota_amostra = amostra['Nota'].mean()
print(f"Média da idade da amostra: {media_idade_amostra}")
print(f"Média da nota da amostra: {media_nota_amostra}")

# Selecione uma amostra aleatória de 10 alunos
amostra_10 = alunos.sample(n=10)
print("Amostra aleatória de 10 alunos:")
print(amostra_10)

# Calcule a média da amostra para idade e nota
media_idade_amostra_10 = amostra_10['Idade'].mean()
media_nota_amostra_10 = amostra_10['Nota'].mean()
print(f"Média da idade da amostra de 10 alunos: {media_idade_amostra_10}")
print(f"Média da nota da amostra de 10 alunos: {media_nota_amostra_10}")

#compare as medias da população com as médias das amostras e erro amostral
erro_amostral_idade_5 = abs(media_idade_populacao - media_idade_amostra)
erro_amostral_nota_5 = abs(media_nota_populacao - media_nota_amostra)
erro_amostral_idade_10 = abs(media_idade_populacao - media_idade_amostra_10)
erro_amostral_nota_10 = abs(media_nota_populacao - media_nota_amostra_10)
print(f"Erro amostral da idade da amostra de 5 alunos: {erro_amostral_idade_5}")
print(f"Erro amostral da nota da amostra de 5 alunos: {erro_amostral_nota_5}")
print(f"Erro amostral da idade da amostra de 10 alunos: {erro_amostral_idade_10}")
print(f"Erro amostral da nota da amostra de 10 alunos: {erro_amostral_nota_10}")    
print("\nComparação das médias:") 
print(f"População - Idade: {media_idade_populacao}, Nota: {media_nota_populacao}")
print(f"Amostra de 5 alunos - Idade: {media_idade_amostra}, Nota: {media_nota_amostra}")
print(f"Amostra de 10 alunos - Idade: {media_idade_amostra_10}, Nota: {media_nota_amostra_10}")
