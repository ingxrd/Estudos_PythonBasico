'''
Utilizando listas faça um programa que faça 5 perguntas para uma
pessoa sobre um crime.
As perguntas são:
""Telefonou para a vítima?""
""Esteve no local do crime?""
""Mora perto da vítima?""
""Devia para a vítima?""
""Já trabalhou com a vítima?""
'''

# Criação de uma lista para armazenar as respostas
respostas = []

# Perguntas a serem feitas
perguntas = [
    "Telefonou para a vítima?",
    "Esteve no local do crime?",
    "Mora perto da vítima?",
    "Devia para a vítima?",
    "Já trabalhou com a vítima?"
]

# Coleta das respostas
for pergunta in perguntas:
    resposta = input(pergunta + " (sim/não) ").strip().lower()
    while resposta not in ["sim", "não"]:
        print("Resposta inválida. Por favor, responda com 'sim' ou 'não'.")
        resposta = input(pergunta + " (sim/não) ").strip().lower()
    respostas.append(resposta)

# Contagem das respostas positivas
num_sim = respostas.count("sim")

# Exibição das respostas
print("\nRespostas coletadas:")
for pergunta, resposta in zip(perguntas, respostas):
    print(f"{pergunta} {resposta}")

# Análise e classificação
if num_sim == 2:
    classificacao = "Suspeita"
elif num_sim in [3, 4]:
    classificacao = "Cúmplice"
elif num_sim == 5:
    classificacao = "Assassino"
else:
    classificacao = "Inocente"

print(f"\nClassificação: {classificacao}")
