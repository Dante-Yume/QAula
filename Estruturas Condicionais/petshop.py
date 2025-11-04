def idade_cachorro(idade_humana):
    return idade_humana * 7


def calcular_lucro(porte, qtd_banhos):
    
    if porte.lower() == "grande":
        valor_banho = 75
        custo_banho = 20
    elif porte.lower() == "medio":
        valor_banho = 60
        custo_banho = 15
    elif porte.lower() == "pequeno":
        valor_banho = 50
        custo_banho = 5
    else:
        print("⚠️ Porte inválido! Use: grande, medio ou pequeno.")
        return None

    lucro = (valor_banho - custo_banho) * qtd_banhos
    return lucro


nome = input("Digite o nome do cachorro: ")
idade_humana = int(input("Digite a idade humana do cachorro: "))
porte = input("Digite o porte do cachorro (grande, medio ou pequeno): ")
qtd_banhos = int(input("Digite a quantidade de banhos em 12 meses: "))


idade_pet = idade_cachorro(idade_humana)
lucro_total = calcular_lucro(porte, qtd_banhos)


if lucro_total is not None:
    print(f"\nOlá, {nome} tem {idade_pet} anos em idade de cachorro e, "
          f"nos últimos 12 meses, o lucro com este animal foi de R${lucro_total:.2f}.")