from modelos.cardapio.item_cardapio import ItemCardapio


class Prato(ItemCardapio):
    def __init__(self, nome, preco, descricao):
        super().__init__(nome, preco)
        self._descricao = descricao
    
    def __str__(self):
        return f'{super().__str__()} - {self._descricao}'
       
    @property
    def descricao(self):
        return self._descricao
    
    @descricao.setter
    def descricao(self, descricao):
        self._descricao = descricao
        
    def aplicar_desconto(self):
        self._preco = self._preco * 0.9