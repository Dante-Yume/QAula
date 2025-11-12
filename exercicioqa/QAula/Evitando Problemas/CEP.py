import requests

integrantes = { }

while True:
    nome = input("Digite o nome de usuário: ")
    cep = input("Digite o CEP do usuário: ")
    integrantes[nome] = cep
    resposta = input("Deseja adicionar outro usuario? (s/n): ")
    if resposta.lower() != 's':
        break

for nome, cep in integrantes.items():
    url = f"https://viacep.com.br/ws/{cep}/json/"
    resposta = requests.get(url)

    if resposta.status_code == 200:
        dados = resposta.json()
        cidade = dados.get("localidade", "Cidade não encontrada")
        print(f'{nome} mora na cidade {cidade}')
    else:
        print(f"Não foi possivel obter os dados para o CEP {cep}.")