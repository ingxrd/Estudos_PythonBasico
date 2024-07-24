'''
Crie um programa que solicite ao usuário um login e uma senha. O
programa deve permitir o acesso apenas se o usuário for "admin" e a senha
for "admin123", caso contrário imprima uma mensagem de erro
'''

login = input("Insira seu login: ")
senha = input("Insira sua senha")

if login != "admin" or senha != "admin123":
    print("Erro. Digite login e senha correto")
else:
    print("Login feito com sucesso")
