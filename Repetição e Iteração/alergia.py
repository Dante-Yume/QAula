frutas = ['maçã', 'banana', 'mamão', 'kiwi']

alergia = []

alergia.append('banana')

for fruta in frutas:
    if fruta in alergia:
        print(f'ATENÇÃO! Você é alergico(a) a {fruta}.')