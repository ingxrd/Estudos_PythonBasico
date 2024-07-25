def conversor_cambio(valor, taxa_conversao):
    return valor / taxa_conversao

def menu():
    print("Bem vinda ao seu câmbio pessoal! Nós convertemos:")
    print("1. Real para Dólar Americano")
    print("2. Real para Dólar Canadense")
    print("3. Real para Franco Suiço")
    print("4. Real para Euro")
    print("5. Real para Libra Esterlina")

    opcao = input("Digite o número da opção escolhida: ")

    taxa_conversao = { #usando dicionário
        '1': 4.91,  # Dólar Americano
        '2': 3.64,  # Dólar Canadense
        '3': 0.42,  # Franco Suiço
        '4': 5.36,  # Euro
        '5': 6.21   # Libra Esterlina
    }

    if opcao in taxa_conversao:
        real = float(input("Insira o seu montante de dinheiro em R$: "))
        valor_convertido = conversor_cambio(real, taxa_conversao[opcao])
        moedas = {
            '1': 'Dólar Americano',
            '2': 'Dólar Canadense',
            '3': 'Franco Suiço',
            '4': 'Euro',
            '5': 'Libra Esterlina'
        }
        print(f"Com R$ {real:.2f}, você pode comprar {valor_convertido:.2f} {moedas[opcao]}.")
    else:
        print("Opção inválida. Tente novamente.")

# Executa o menu
menu()
