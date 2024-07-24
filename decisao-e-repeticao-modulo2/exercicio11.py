'''
10. Faça um programa que lê três números inteiros e os mostra em ordem
crescente.
'''

num1 = int(input("Insira o primeiro número: "))
num2 = int(input("Insira o segundo número: "))
num3 = int(input("Insira o terceiro número: "))

if num1 <= num2 and num1 <= num3:
    menor = num1
    if num2 <= num3:
        intermediario = num2
        maior = num3
    else:
        intermediario = num3
        maior = num2
elif num2 <= num1 and num2 <= num3:
    menor = num2
    if num1 <= num3:
        intermediario = num1
        maior = num3
    else:
        intermediario = num3
        maior = num1
else:
    menor = num3
    if num1 <= num2:
        intermediario = num1
        maior = num2
    else:
        intermediario = num2
        maior = num1

# Mostra os números em ordem crescente
print(f"Os números em ordem crescente são: {menor}, {intermediario}, {maior}")
