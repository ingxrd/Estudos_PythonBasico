#Escreva um programa que calcule o tempo de uma viagem. Faça um comparativo do mesmo percurso de
    # avião 600km/h
    # carro 100km/h
    # onibus 80km/h

distancia = int(input("Insira a distância em KM para saber o tempo de viagem: "))
aviao = distancia/600
carro = distancia/100
onibus = distancia/80

print(f'O tempo de viagem é: \n Avião: {aviao:.2f} \n carro: {carro:.2f} \n onibus: {onibus:.2f}')