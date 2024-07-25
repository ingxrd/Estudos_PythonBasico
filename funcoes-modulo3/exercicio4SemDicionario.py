def menu():
    print("Escolha a conversão desejada:")
    print("1. Real para Dólar Americano")
    print("2. Real para Dólar Canadense")
    print("3. Real para Franco Suiço")
    print("4. Real para Euro")
    print("5. Real para Libra Esterlina")

    opcao = input("Digite o número da opção escolhida: ")
    real = float(input("Insira o seu montante de dinheiro em R$: "))

    if opcao == '1':
        valor_convertido = real / 4.91
        moeda = 'Dólar Americano'
    elif opcao == '2':
        valor_convertido = real / 3.64
        moeda = 'Dólar Canadense'
    elif opcao == '3':
        valor_convertido = real / 0.42
        moeda = 'Franco Suiço'
    elif opcao == '4':
        valor_convertido = real / 5.36
        moeda = 'Euro'
    elif opcao == '5':
        valor_convertido = real / 6.21
        moeda = 'Libra Esterlina'
    else:
        print("Opção inválida. Tente novamente.")
        return

    print(f"Com R$ {real:.2f}, você pode comprar {valor_convertido:.2f} {moeda}.")
menu()