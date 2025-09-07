from modelos.restaurante import Restaurante
from modelos.cardapio.prato import Prato
from modelos.cardapio.bebida import Bebida

import os
import requests
import json


url = 'https://guilhermeonrails.github.io/api-restaurantes/restaurantes.json'
response = requests.get(url)

if response.status_code == 200:
    print('Requisição bem sucedida!')
    dados_json = response.json()
    dados_restaurantes = {}
    for item in dados_json:
        nome_restaurante = item['Company']
        if nome_restaurante not in dados_restaurantes:
            dados_restaurantes[nome_restaurante] = []
        dados_restaurantes[nome_restaurante].append({
            "item": item['Item'],
            "preco": item['price'],
            "descricao": item['description']
        })
    for nome_do_restaurante, dados in dados_restaurantes.items():
        nome_do_arquivo = f'{nome_do_restaurante}.json'
        with open(nome_do_arquivo,'w') as arquivo_restaurante:
            json.dump(dados,arquivo_restaurante,indent=4)
else:
    print(f'Requisição falhou! - Status code: {response.status_code}')







# restaurante_praca = Restaurante('praça', 'Gourmet')
# bebida_suco = Bebida('Suco de Laranja',10.50, 'Grande')
# prato_coxinha = Prato('Coxinha',5.00, 'Coxinha de frango recheada com requeijão')
# restaurante_praca.adicionar_item_cardapio(bebida_suco)
# restaurante_praca.adicionar_item_cardapio(prato_coxinha)
# restaurante_praca.adicionar_item_cardapio(Bebida('Coca-Cola',5.50, '350ml'))
# restaurante_praca.adicionar_item_cardapio(Bebida('Fanta',5.50, '350ml'))
# restaurante_praca.adicionar_item_cardapio(Prato('Pastel',8, 'Pastel de carne'))
# restaurante_praca.receber_avaliacao('Gui', 10)
# restaurante_praca.receber_avaliacao('Lais', 8)
# restaurante_praca.receber_avaliacao('Emy', 2)

# def main():
#     os.system('cls')
#     restaurante_praca._cardapio[0].aplicar_desconto()
#     restaurante_praca.listar_cardapio()
    

# if __name__ == '__main__':
#     main()