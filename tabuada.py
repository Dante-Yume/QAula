numero = int(input('digite um numero para ver a tabuada: '))

print(f'\nTabuada do {numero}:\n')
for i in range (1, 11):
    resultado = numero * i
    print(f'{numero} x {i} = {resultado}')
    print("\nTabuada concluida!")