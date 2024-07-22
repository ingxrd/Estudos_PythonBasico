#Receba do usuário a quantidade de litros de combustível consumidos e a distância percorrida. Calcule e imprima o consumo médio em km/l

qntLitros = int(input("Insira a quantidade de litros: "))
distancia = int(input("Insira a distância percorrida: "))
calculo = qntLitros / distancia
print(f' O consumo médio é de  {calculo:.2f}')