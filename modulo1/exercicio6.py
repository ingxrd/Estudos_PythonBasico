#Solicite ao usuário o seu peso em KG e a altura em metros. Calcule e imprima o IMC usando a formula IMC = peso / (altura*altura)

altura = float(input("Insira sua altura (em metros): "))
peso = float(input("Insira seu peso: "))

imc = (peso / (altura**2))

print(f' Seu IMC é de {imc:.2f}')