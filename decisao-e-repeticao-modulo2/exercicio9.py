'''
Criar um programa em Python que solicite três números ao usuário, utilize
estruturas condicionais para determinar o maior entre eles e apresente o
resultado
'''

num1 = int(input("Insira numero 1: "))
num2 = int(input("Insira numero 2: "))
num3 = int(input("Insira numero 3: "))

if num1 >= num2 or num1 >= num3:
    print(f'O maior número é: {num1}')
elif num2 >= num1 or num2 >= num3:
    print(f'O maior número é: {num2}')
else:
    print(f'O maior número é: {num3}')


