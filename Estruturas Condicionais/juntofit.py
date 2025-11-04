'''
Na "JUNTOFIT", se um aluno tiver frequência de 21 vezes, sem interrupções, ele ganha um mês de aulas gratuitas para presentear um acompanhante. Caso contrário, ele não se qualifica para o benefício.

Na catraca de acesso, haverá uma tela voltada para o cliente. Todos os dias, quando ele passar, deve aparecer a mensagem "VOCÊ ESTÁ PARTICIPANDO DA NOSSA PROMO TREINA JUNTO"

Quando ele completar 21 identificações seguidas, deve aparecer a mensagem "UHUU. AGORA VOCÊ PODE PRESENTEAR UM AMIGO OU AMIGA PARA TREINAR COM VOCÊ".

Caso o cliente tenha uma certa frequência, mas falte algum dia, quando retornar, deve aparecer "QUE BOM VER VOCÊ DE VOLTA. A PARTIR DE AGORA INICIAMOS MAIS UMA CONTAGEM DE 21 DIAS PARA A PROMO TREINA JUNTO."
'''

print("VOCÊ ESTÁ PARTICIPANDO DA NOSSA PROMO TREINA JUNTO: " )
F= int(input("frequencia do usuario: " ))
if F> 20:
    print("UHUU. AGORA VOCÊ PODE PRESENTEAR UM AMIGO OU AMIGA PARA TREINAR COM VOCÊ")
elif F> 19 < 20: 
    print("QUE BOM VER VOCÊ DE VOLTA. A PARTIR DE AGORA INICIAMOS MAIS UMA CONTAGEM DE 21 DIAS PARA A PROMO TREINA JUNTO.")
else: print('O USUARIO NÃO ESTÁ QUALIFICADO PARA NOSSA PROMO TREINA JUNTO')