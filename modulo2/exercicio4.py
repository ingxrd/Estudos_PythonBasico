'''
Faça um programa que pergunte em que turno você estuda. Peça para digitar:

M - Matutino
V - Vespertino
N - Noturno

Imprima a mensagem:
    "Bom Dia!" para o turno Matutino
    "Boa Tarde!" para o turno Vespertino
    "Boa Noite!" para o turno Noturno
    "Valor Inválido!" caso o valor seja inválido
'''

while True:
    turno = input('Qual turno você estuda? \n [M] - Matutino\n [V] - Vespertino\n [N] - Noturno ')
    if turno == 'M'.lower():
        print("Bom dia!")
    elif turno == 'V'.lower():
        print("Boa tarde!")
    elif turno == 'N'.lower():
        print("Boa noite!")
    else:
        print("Valor inválido!")
