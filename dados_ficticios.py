import pandas as pd


df = pd.read_csv("/mnt/data/dados_ficticios (1).csv")


filtro_idade = df[df["idade"] > 40]
print("Pessoas com idade > 40:\n", filtro_idade, "\n")


filtro_renda_5k = df[df["renda"] > 5000]
print("Pessoas com renda > 5000:\n", filtro_renda_5k, "\n")


filtro_renda_15k = df[df["renda"] > 15000]
print("Pessoas com renda > 15000:\n", filtro_renda_15k)