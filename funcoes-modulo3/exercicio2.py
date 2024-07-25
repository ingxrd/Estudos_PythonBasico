'''
Reverso do número. Faça uma função que retorne o reverso de um
número inteiro informado. Por exemplo: 127 -> 721
'''


def inversorNumero(num):
    num_str = str(num) #converte numero pra uma string
    invertendoNumero = num_str[::-1] #inverte a string
    return int(invertendoNumero) #o retorno é a inversão de string pra numero

inversao = inversorNumero(123)
print(inversao)

