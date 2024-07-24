'''
Desenvolver um programa que solicite a idade do usuário e identifique se
ele é uma criança, um adolescente, adulto ou idoso.
'''

idade = int(input("Insira sua idade"))


if idade >= 60:
    print("Você é idoso")
elif idade >= 18:
    print("Você é adulto")
elif idade >= 13:
    print("Você é adolescente")
else:
    print("Você é criança")
