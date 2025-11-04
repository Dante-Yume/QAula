from faker import Faker
import random
import pandas as pd

fake = Faker('pt_BR')


def criar_personas(qtd):
    personas = []

    for _ in range(qtd):
        pessoa = {
            "Nome": fake.name(),
            "Cidade": fake.city(),
            "Idade": random.randint(18, 70)
        }
        personas.append(pessoa)

    return personas


lista_personas = criar_personas(10)


df = pd.DataFrame(lista_personas)


df.to_csv("personas.csv", index=False, encoding="utf-8-sig")

print("✅ Arquivo 'personas.csv' criado com sucesso!")
print(df)