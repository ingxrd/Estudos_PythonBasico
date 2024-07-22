#Faça um programa que peça uma nota, entre zero e dez.
# #Mostre uma mensagem caso o valor seja inválido e continue pedindo até que o usuário informe um valor válido.

while True:
    nota = int(input("Digite uma nota entre 0 e dez"))
    if nota > 10 or nota < 0:
        nota = int(input("Por favor, digite um número entre 0 e 10"))
    else:
        print(f' Nota: {nota}')
        break