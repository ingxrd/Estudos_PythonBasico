#Faça um programa que peça dois números, realize as principais operações: soma, subtração, multiplicação e divisão.


numero1 = int(input("Digite um número para operação: "))
numero2 = int(input("Digite o segundo número para operação: "))

soma = numero1 + numero2
subtracao = numero1 - numero2
multiplicacao = numero1 * numero2
divisao = numero1 / numero2


while True:
    opcoesMenu = input("\nSelecione a opção desejada: \n1. Soma \n2. Subtração \n3. Multiplicação \n4. Divisão \n5. Finalize a aplicação.")
    if opcoesMenu == '1':
        print("Resultado:", soma)
    elif opcoesMenu == '2':
        print("Resultado:",subtracao)
    elif opcoesMenu == '3':
        print("Resultado:",multiplicacao)
    elif opcoesMenu == '4':
        print("Resultado:",divisao)
    else:
        break