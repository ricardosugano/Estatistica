import pandas as pd

dados = {
    "produto": ["Notebook", "Smartphone", "Tablet", "Monitor"],
    "categoria": ["Eletrônicos", "Eletrônicos", "Eletrônicos", "Periféricos"],
    "preço": [2500, 1500, 800, 1200],
    "estoque": [10, 25, 15, 20]
}

df= pd.DataFrame(dados)

print(df)

print(df.shape)

print(df.describe())

print(df.info())

print(df[["produto", "preço"]])

print(df.iloc[0:2])

print(df.iloc[df["preço"].idxmax()])