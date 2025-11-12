def verificar_grupo(matricula):
    if matricula % 2 == 0:
        return "VOCÊ ESTÁ NO TIME AZUL"
    else:
        return "VOCÊ ESTÁ NO TIME AMARELO"

matriculas = []

while len(matriculas) < 5:
    try:
        numero = int(input(f"Digite o número de matrícula ({len(matriculas)+1}/5): "))
        matriculas.append(numero)
    except ValueError:
        print("❌ Por favor, digite apenas números inteiros.")

print("\nMatrículas registradas:", matriculas)
print("------------------------------------------------")

for matricula in matriculas:
    resultado = verificar_grupo(matricula)
    print(f"Matrícula {matricula}: {resultado}")