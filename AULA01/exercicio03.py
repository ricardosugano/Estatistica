import matplotlib.pyplot as plt
import pandas as pd
dados = {
    'Produto': ["Calçado", "Camisa", "Calça", "Blusa", "Vestido"],
    "Preço": [100, 50, 80, 60, 120],
    "Quantidade": [10, 20, 15, 25, 5]
}
df = pd.DataFrame(dados)
df.info()

print(len(df))

#gráfico de barras
plt.bar(df['Produto'], df['Preço'], color='red',
        )
plt.title("Gráfico de Barras")
plt.xlabel("Produto")
plt.ylabel("Preço")

#plt.bar(df['Produto'], df['Quantidade'])

#gráfico pizza
#plt.pie(df['Preço'], labels=df['Produto'], autopct='%1.1f%%')

#gráfico de barras horizontais
#plt.barh(df['Produto'], df['Preço'])

#gráfico de linhas
#plt.plot(df['Produto'], df['Preço'])

#gráfico de dispersão
#plt.scatter(df['Produto'], df['Preço'])

plt.show()
