'''
Crie um dicionário representando contatos (nome, telefone).
Permita ao usuário procurar por um contato pelo nome.
'''

listaTelefonica = {
    'Ingrid': 11934678990,
    'William': 1234676990
}

procurarContato = input('Insira o nome do seu contato: ')

if procurarContato not in listaTelefonica:
    print("Usuário não está na lista")
else:
    telefone = listaTelefonica[procurarContato]
    print(f"Telefone de {procurarContato}: {telefone}")



