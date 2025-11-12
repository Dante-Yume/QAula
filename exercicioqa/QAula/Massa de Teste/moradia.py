import pandas as pd


dados = {
    "Nome": ["Ana", "Carlos", "Beatriz", "Lucas", "Fernanda", "João", "Marina"],
    "Idade": [25, 32, 28, 40, 22, 35, 27],
    "Cidade": ["Recife", "Recife", "Recife", "Salvador", "Salvador", "São Paulo", "Manaus"]
}

tabela = pd.DataFrame(dados)


print("Tabela completa:\n")
print(tabela)


recife = tabela[tabela["Cidade"] == "Recife"]

print("\n Moradores de Recife:\n")
print(recife)