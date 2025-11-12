import pandas as pd


dados = {
    "Nome": ["João", "Marta", "Ary", "Matheus", "Michele"],
    "Idade": [51, 37, 23, 24, 33]
}


tabela = pd.DataFrame(dados)


print(tabela)