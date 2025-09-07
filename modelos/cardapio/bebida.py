from modelos.cardapio.item_cardapio import ItemCardapio

class Bebida(ItemCardapio):
    def __init__(self, nome, preco, tamanho):
        super().__init__(nome, preco)
        self._tamanho = tamanho

    def __str__(self):
        return f'{super().__str__()} - {self._tamanho}'
    
    @property
    def tamanho(self):
        return self._tamanho
    
    @tamanho.setter
    def tamanho(self, tamanho):
        self._tamanho = tamanho


    def aplicar_desconto(self):
        self._preco = self._preco * 0.95

