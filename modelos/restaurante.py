
from modelos.cardapio.item_cardapio import ItemCardapio
from modelos.avaliacao import Avaliacao

class Restaurante:
    restaurantes = []

    def __init__(self, nome, categoria):
        self._nome = nome.title()
        self._categoria = categoria.upper()
        self._ativo = False
        self._avaliacao = []
        self._cardapio = []
        Restaurante.restaurantes.append(self)
    
    def __str__(self):
        return f'{self._nome} | {self._categoria}'
    
    @classmethod
    def listar_restaurantes(cls):
        print(f'{"Nome do restaurante".ljust(25)} | {"Categoria".ljust(25)} | {"Avaliação".ljust(25)} |{"Status"}')
        for restaurante in cls.restaurantes:
            print(f'{restaurante._nome.ljust(25)} | {restaurante._categoria.ljust(25)} | {str(restaurante.media_avaliacoes).ljust(25)} |{restaurante.ativo}')

    @property
    def ativo(self):
        return '⌧' if self._ativo else '☐'
    
    def alternar_estado(self):
        self._ativo = not self._ativo

    def receber_avaliacao(self, cliente, nota):
        if 0 < nota <= 5: 
            avaliacao = Avaliacao(cliente, nota)
            self._avaliacao.append(avaliacao)

    @property
    def media_avaliacoes(self):
        if not self._avaliacao:
            return '-'
        soma_das_notas = sum(avaliacao._nota for avaliacao in self._avaliacao)
        quantidade_de_notas = len(self._avaliacao)
        media = round(soma_das_notas / quantidade_de_notas, 1)
        return media
    
    def adicionar_item_cardapio(self, item):
        if isinstance(item, ItemCardapio):
            self._cardapio.append(item)
    
    def remover_item_cardapio(self, item):
        self._cardapio.remove(item)
        
    def listar_cardapio(self):
        print(f'Cardápio do restaurante {self._nome}')
        mensagem_prato = ''
        mensagem_bebida = ''
        prato = 0
        bebida = 0
        for item in self._cardapio:
            if hasattr(item,'descricao'):
                prato = prato + 1
                mensagem_prato += f'{prato} - ' + item.__str__() + '\n'
            else:
                bebida = bebida + 1
                mensagem_bebida +=  f'{bebida} - ' + item.__str__() + '\n'

        print('PRATOS:\n')
        print(mensagem_prato)
        print('BEBIDAS:\n')
        print(mensagem_bebida)