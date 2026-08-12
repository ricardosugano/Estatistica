#import pandas as pd

#dados = {
#    'Aluno': ['Ana', 'Bruno', 'Carlos', 'Diana'],
#    "Idade": [20, 22, 21, 23],
#    "Nota": [8.5, 7.0, 9.0, 6.5]
#}

#df = pd.DataFrame(dados)
 
#df["Nota_Final"] = df["Nota"] + 1.3 

#df.info()
#print(df.describe())

#import pandas as pd

#dados = {
#    "Produto": ["Notebook", "Smartphone", "Tablet", "Monitor"],
#    "Preço": [2500, 1500, 800, 1200],
#    "Estoque": [10, 25, 15, 20]
#}

#df = pd.DataFrame(dados)
#df["Preço_Final"] = df["Preço"] * 1.2

#print(df.sort_values(by="Preço_Final", ascending=True))

#print(df[df["Estoque"] > 15])

import pandas as pd

df = pd.read_csv("dados.csv")

print(df.describe())

