import pandas as pd
dados = {
    'numeros': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
}
df = pd.DataFrame(dados)
df.info()

#quantidade de elementos, soma, maior valor, menor valor
print(len(df))
print(df['numeros'].sum())
print(df['numeros'].max())
print(df['numeros'].min())

#sem usar df

seuqencia = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(f"Quantidade de elementos: {len(seuqencia)}")
print(f"Soma: {sum(seuqencia)}")
print(f"Maior valor: {max(seuqencia)}")
print(f"Menor valor: {min(seuqencia)}")
