'''
6. Vamos construir um jogo de forca. O programa escolherá
aleatoriamente uma palavra secreta de uma lista predefinida. A palavra
secreta será representada por espaços em branco, um para cada letra
da palavra. O jogador terá um número limitado de 6 tentativas. Em cada
tentativa, o jogador pode fornecer uma letra. Se a letra estiver presente
na palavra secreta, ela será revelada nas posições correspondentes. Se
a letra não estiver na palavra, uma mensagem de erro deverá ser
informada. Após um número máximo de erros, o jogador perde. O jogo
continua até que o jogador adivinhe a palavra ou exceda o número
máximo de tentativas.
Dica: Você precisará importar uma biblioteca para resolver esse
exercício
'''

import random


def escolher_palavra():
    lista_palavras = ['womakerscode', 'mulheres', 'na', 'tecnologia']
    return random.choice(lista_palavras)


def mostrar_palavra(palavra_secreta, letras_corretas):
    return ' '.join([letra if letra in letras_corretas else '_' for letra in palavra_secreta])


def jogo_forca():
    palavra_secreta = escolher_palavra()
    letras_corretas = set()
    tentativas_erradas = 0
    tentativas_maximas = 6

    print("Bem-vindo ao Jogo da Forca!")
    print("Adivinhe a palavra:")

    while tentativas_erradas < tentativas_maximas:
        print(mostrar_palavra(palavra_secreta, letras_corretas))
        tentativa = input("Digite uma letra: ").lower()

        if len(tentativa) != 1 or not tentativa.isalpha():
            print("Por favor, digite uma única letra.")
            continue

        if tentativa in letras_corretas:
            print("Você já tentou essa letra.")
            continue

        if tentativa in palavra_secreta:
            letras_corretas.add(tentativa)
            print("Uhul! A letra está na palavra.")
        else:
            tentativas_erradas += 1
            print(f"Letra incorreta! Você tem {tentativas_maximas - tentativas_erradas} tentativas restantes.")

        if all(letra in letras_corretas for letra in palavra_secreta):
            print(f"Parabéns! Você adivinhou a palavra: {palavra_secreta}")
            break
    else:
        print(f"Game Over! A palavra era: {palavra_secreta}")


# Inicia o jogo
jogo_forca()

