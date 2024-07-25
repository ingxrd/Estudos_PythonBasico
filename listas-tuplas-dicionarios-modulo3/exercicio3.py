'''
Crie um dicionário representando um carrinho de compras.
Adicione produtos (chaves) e quantidades (valores) ao carrinho.
Calcule o total do carrinho de compra.
'''

carrinho_Compras = {}

carrinho_Compras['nintendo switch'] = 1900
carrinho_Compras['livros'] = 200

total = sum(carrinho_Compras.values())
print(carrinho_Compras)
print(f"Total do carrinho de compras: R${total}")
