import matplotlib.pyplot as plt
import pandas as pd
dados = {
    'Produto': ["Arroz", "Feijão", "Café", "Macarrão", "Açúcar", "Sal", "Óleo", "Leite", "Manteiga", "Pão"],
    "Preço": [32, 11, 24, 6, 8, 9, 7, 15, 20, 12]
}
df = pd.DataFrame(dados)
df.info()

#gráfico de barras
plt.bar(df['Produto'], df['Preço'], color='blue')
plt.title("Gráfico de Barras")
plt.xlabel("Produto")
plt.ylabel("Preço")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

