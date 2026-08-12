import matplotlib.pyplot as plt
import pandas as pd
dados = {
    'Filmes': ["Vingadores: Ultimato", "Avatar", "Titanic", "Star Wars: O Despertar da Força", "Jurassic World", "O Rei Leão", "Os Incríveis 2", "Vingadores: Guerra Infinita", "Frozen II", "Harry Potter e as Relíquias da Morte - Parte 2"],
    "Nota": [9.2, 9.5, 8.6, 8.9, 7.8, 9.8, 8.95, 10, 8.5, 9.0]
}
df = pd.DataFrame(dados)
df.info()


#gráfico de barras
plt.bar(df['Filmes'], df['Nota'], color='blue')
plt.title("Gráfico de Barras")
plt.xlabel("Filmes")
plt.ylabel("Nota")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()