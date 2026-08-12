import pandas as pd

dados = {
    "produto": ["Notebook", "Smartphone", "Tablet", "Monitor"],
    "categoria": ["Eletrônicos", "Eletrônicos", "Eletrônicos", "Periféricos"],
    "preço": [2500, 1500, 800, 1200],
    "estoque": [10, 25, 15, 20]
}

df= pd.DataFrame(dados)

df["Valor_Estoque"] = df["estoque"] * df["preço"] 

print(df)

print("Qual é o produto com maior valor de estoque?")
print(df.iloc[df["Valor_Estoque"].idxmax()])

print("Qual é o produto com menor valor de estoque?")
print(df.iloc[df["Valor_Estoque"].idxmin()])

print("Qual é o valor total do estoque?")
print(df["Valor_Estoque"].sum())


