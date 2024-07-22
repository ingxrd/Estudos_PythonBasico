exercicioSemanalHoras = int(input("Digite o número de horas de exercício físico semanal: "))

exercicioSemanalMinutos = exercicioSemanalHoras * 60
totalCalorias = exercicioSemanalMinutos * 5 * 4
print(f"Total de calorias queimadas em um mês: {totalCalorias}")
