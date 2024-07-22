#Faça um programa que peça dois números e imprima o maior deles.

numero1 = int(input("Insira um número: "))
numero2 = int(input("Insira outro número: "))

if numero1 > numero2:
    print(f'O maior número é: {numero1}')
elif numero2 > numero1:
    print(f'O maior número é: {numero2}')
else:
    print('Os números são iguais.')