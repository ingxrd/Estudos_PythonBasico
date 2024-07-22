#Faça um programa que peça a quantidade de quilômetros, transforme em metros, centímetros e milímetros



while True:
    opcoesMenu = input("Bem vindo ao seu conversor pessoal. Selecione a opção desejada. \n1. KM para Metros. \n2. Centímetros para Milímetros\n")
    if opcoesMenu == '1':
        km = int(input("Insira KM: "))
        calculoKM = km * 1000
        print(f'{km} km é {calculoKM} metros')
    elif opcoesMenu == '2':
        cm = int(input("Insira CM: "))
        calculoMM = cm * 10
        print(f'{cm} cm é {calculoMM} milímetros')
    else:
        break
