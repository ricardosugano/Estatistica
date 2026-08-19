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

