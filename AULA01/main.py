#nosso primeiro DataFrame
import pandas as pd

dados = {
    'Aluno': ['Ana', 'Bruno', 'Carlos', 'Diana'],
    "Nota": [8.5, 7.0, 9.0, 6.5]
}

df = pd.DataFrame(dados)

df.info()

print(df.describe())

print(df.head())

