#Faça um programa que pergunte quanto voce ganha por hora e o numero de horas trabalhadas no mes.
# Calcule e mostre o total do seu salario no referido mes

valorHora = float(input("Insira o valor das horas trabalhadas: "))
horasMes = int(input("Insira as horas trabalhadas no mês: "))

calculoSalario = valorHora * horasMes
print(f'Seu salário do mês é de R${calculoSalario:.2f}')
