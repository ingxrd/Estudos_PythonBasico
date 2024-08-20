from mercado import Mercado
from cliente import Cliente
from fornecedor import Fornecedor
from produto import Produto
from transacao import Transacao

# Exemplo de transação no mercado
if __name__ == "__main__":
    mercado = Mercado()

#Instanciando cliente
cliente = Cliente('Ana', '99999-999', 'Rua fulano sicrano')

#Instanciando produto
produto_arroz = Produto(
    nome_produto='Arroz',
    fornecedores=['Tio João', 'Camil'],
    categoria='Alimentos',
    quantidade_estoque=100
)

# Exibindo informações do cliente e do produto
print(cliente)
print(produto_arroz)

# Criando uma transação e registrando-a
transacao = Transacao(cliente, produto_arroz, 20)
mercado = Mercado()
mercado.adicionar_cliente(cliente)
mercado.adicionar_produto(produto_arroz)
mercado.registrar_transacao(transacao)

# Exibindo informações após a venda
print(produto_arroz)
print(transacao)

# Criando uma instância de Fornecedor
fornecedor = Fornecedor('Fornecedor X', 'Av. Central, 123', '123.456.789/0001-00')
print(fornecedor.nome, fornecedor.endereco, fornecedor.cnpj)