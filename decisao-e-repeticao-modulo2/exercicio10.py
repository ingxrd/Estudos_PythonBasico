'''
9. O programa deve calcular e apresentar a quantidade de números pares e
ímpares inseridos. O processo de leitura deve ser encerrado quando o usuário
informar o valor zero. Certifique-se de incluir validações para garantir que
apenas números positivos sejam considerados na contagem e cálculos
'''

contPar = 0
contImpar = 0

while True:
    numero = int(input("Insira um número. Insira 0 para fechar o programa: "))

    if numero == 0:
        break
    elif numero > 0:
        if numero % 2 == 0:
            contPar += 1
        else:
            contImpar += 1
    else:
        print("Insira apenas números positivos")

print(f'Total de números pares: {contPar}')
print(f'Total de números ímpares: {contImpar}')
