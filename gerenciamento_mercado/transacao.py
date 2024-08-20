from datetime import datetime

class Transacao:
    def __init__(self, cliente, produto, quantidade):
        self.data = datetime.now()
        self.cliente = cliente
        self.produto = produto
        self.quantidade = quantidade
        
    def concluir_transacao(self):
        # Verifica se há estoque suficiente e conclui a transação
        if self.quantidade > self.produto.quantidade_estoque:
            raise ValueError("Quantidade insuficiente em estoque para concluir a transação.")
        self.produto.quantidade_estoque -= self.quantidade
        print(f"Transação concluída: {self.quantidade} unidades de {self.produto.nome_produto} vendidas para {self.cliente.nome}.")

    def __str__(self):
        return f"Data: {self.data} - Cliente: {self.cliente.nome} - Produto: {self.produto.nome_produto} - Quantidade: {self.quantidade}"
