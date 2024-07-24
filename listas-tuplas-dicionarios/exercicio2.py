'''
Faça um Programa que peça as quatro notas de 5 alunos, calcule
e armazene numa lista a média de cada aluno, imprima o número
de alunos com média maior ou igual a 7.0
'''


#começo com uma lista vazia para guardar as médias, conforme realizar a conta
medias = []

#vou usar a sintaxe for, para adicionar as informações a media
for i in range(5):

    # aqui, peço as notas aos alunos
    notas = [float(input(f"Aluno {i + 1} - Nota {j + 1}: ")) for j in range(4)]

    #depois, eu calculo a media usando o belissimo método SUM
    #em seguida, vou uar LEN para contar quantas notas tem em notas
    media = sum(notas) / len(notas)

    # Armazena a média
    medias.append(media)

# Conta o número de alunos com média maior ou igual a 7.0
alunosMediaMaiorSete= sum(1 for media in medias if media >= 7.0)

# Imprime o número de alunos com média maior ou igual a 7.0
print(f"Número de alunos com média maior ou igual a 7.0: {alunosMediaMaiorSete}")





