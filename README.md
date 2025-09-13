# API de Cardápios de Restaurantes

![Python](https://img.shields.io/badge/Python-3.11-3776AB?style=for-the-badge&logo=python&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi)

Uma API REST simples, desenvolvida em Python com o framework FastAPI, que fornece dados de cardápios de restaurantes a partir de uma fonte de dados externa.

## 🚀 Sobre o Projeto

Este projeto foi criado para demonstrar a construção de uma API funcional utilizando FastAPI. A API consome um arquivo JSON externo, processa os dados e os expõe através de endpoints RESTful.

## ✨ Funcionalidades

- **Listagem completa:** Retorna o cardápio de todos os restaurantes disponíveis.
- **Filtro por restaurante:** Permite consultar o cardápio de um restaurante específico através de um parâmetro na URL.
- **Documentação automática:** Graças ao FastAPI, a API possui documentação interativa (Swagger UI e ReDoc) gerada automaticamente.

## 🛠️ Tecnologias Utilizadas

- **Python 3.10+**
- **FastAPI:** O framework web para a construção da API.
- **Uvicorn:** O servidor ASGI para executar a aplicação.
- **Requests:** Para realizar chamadas HTTP e obter os dados dos restaurantes.

## ⚙️ Instalação e Execução

Siga os passos abaixo para executar o projeto em sua máquina local.

**1. Clone o repositório**
```bash
git clone https://github.com/juliootto/restaurante.git
cd restaurante
```

**2. Crie um ambiente virtual e ative-o**
```bash
# Para Linux/Mac
python3 -m venv venv
source venv/bin/activate

# Para Windows
python -m venv venv
.\venv\Scripts\activate
```
**3. Crie o arquivo `requirements.txt`**

Crie um arquivo chamado `requirements.txt` na raiz do projeto com o seguinte conteúdo:
```txt
fastapi
uvicorn[standard]
requests
```

**4. Instale as dependências**
```bash
pip install -r requirements.txt
```

**5. Execute a API**
execute o comando abaixo:
```bash
uvicorn main:app --reload
```

O servidor estará rodando em `http://127.0.0.1:8000`. A flag `--reload` reinicia o servidor automaticamente sempre que você fizer alterações no código.

## 📚 Documentação da API

FastAPI gera automaticamente uma documentação interativa. Com o servidor rodando, acesse um dos seguintes links no seu navegador:

- **Swagger UI:** `http://127.0.0.1:8000/docs`
- **ReDoc:** `http://127.0.0.1:8000/redoc`

### Endpoints

#### Endpoint de Teste

- **GET** `/api/hello`
  - **Descrição:** Endpoint simples para verificar se a API está online.
  - **Resposta de Sucesso (200 OK):**
    ```json
    {
      "Hello": "World"
    }
    ```

#### Endpoints de Restaurantes

- **GET** `/api/restaurantes/`
  - **Descrição:** Retorna uma lista com os itens de todos os restaurantes.
  - **Exemplo de uso (curl):**
    ```bash
    curl http://127.0.0.1:8000/api/restaurantes/
    ```
  - **Resposta de Sucesso (200 OK):**
    ```json
    {
      "Dados": [
        {
          "Company": "McDonalds",
          "Item": "Big Mac",
          "price": 5.99,
          "description": "Dois hambúrgueres, alface, queijo..."
        },
        {
          "Company": "Pizza Hut",
          "Item": "Pizza Pepperoni",
          "price": 12.99,
          "description": "Pizza de pepperoni com queijo extra."
        }
      ]
    }
    ```

- **GET** `/api/restaurantes/?restaurante={nome_do_restaurante}`
  - **Descrição:** Retorna o cardápio de um restaurante específico.
  - **Parâmetro (Query):** `restaurante` (string) - O nome do restaurante a ser filtrado (ex: "McDonalds").
  - **Exemplo de uso (curl):**
    ```bash
    curl "http://127.0.0.1:8000/api/restaurantes/?restaurante=McDonalds"
    ```
  - **Resposta de Sucesso (200 OK):**
    ```json
    {
      "Restaurante": "McDonalds",
      "Cardapio": [
        {
          "item": "Big Mac",
          "price": 5.99,
          "description": "Dois hambúrgueres, alface, queijo..."
        },
        {
          "item": "McFlurry",
          "price": 2.49,
          "description": "Sorvete de baunilha com pedaços de Oreo."
        }
      ]
    }
    ```

## 👨‍💻 Autor

Desenvolvido por **Julio Otto**.

- **LinkedIn:** [https://www.linkedin.com/in/julio-cezar-otto-junior-b184502/](https://www.linkedin.com/in/julio-cezar-otto-junior-b184502/)
- **GitHub:** [https://github.com/juliootto](https://github.com/juliootto)
