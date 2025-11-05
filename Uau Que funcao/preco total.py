def calcular_prco_total(valor_total, desconto_percentual):
    desconto = valor_total * (desconto_percentual / 100)
    prco_com_desconto = valor_total - desconto
    return prco_com_desconto

valor_da_compra = 100
desconto_oferecido = 10

preco_final = calcular_prco_total(valor_da_compra, desconto_oferecido)
print(f"O preço total após o desconto de {desconto_oferecido}% é: R${preco_final:.2f}")