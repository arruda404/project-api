# API de Gerenciamento de Itens

## Descrição
Esta aplicação é uma API desenvolvida em Flask para gerenciar itens com deploy no Google Cloud Platform.
Ela permite listar, adicionar, atualizar e excluir itens, com atributos específicos, como nome, valor, data de criação e a identificação de itens eletrônicos.

---
Foi realizado um parâmetro para que seja verificado se e um eletrônico (true) ou não (false).



## Incrementações futuras: 
- I.A para verificar quando o item é ou não Eletrônico. 
- db para armazenamento dos itens e contagens de itens iguais.



## Funcionalidades
A API oferece os seguintes endpoints:
- **`GET /items`** - Listar todos os itens.
- **`POST /items`** - Adicionar um novo item.
- **`PUT /items/<id>`** - Atualizar um item existente.
- **`DELETE /items/<id>`** - Deletar um item existente.

---

## Configuração e Instalação

### Requisitos
- **Python** 3.12 
- **Bibliotecas Python**:
  - Flask
  - Pytest (para testes)

### Passos para Instalação local

1. **Clone o repositório:**
   ```bash
   git clone 
   cd na pasta que foi criada
2. **ambiente virtual:**
   python -m venv venv
   source venv/bin/activate # No Windows: venv\Scripts\activate
3. **Instale as dependências:**
  pip install -r requirements.txt

4. **Execute a aplicação:**
  python.exe app.py



# Testes Automatizados
Para executar os testes, utilize o comando: pytest -vv
---

## Descrição dos Testes
Os testes foram implementados utilizando Pytest para verificar os seguintes casos:

- **Home (GET /)**: Verifica se a API retorna corretamente as informações sobre os endpoints disponíveis.
- **Adicionar Item (POST /items)**: Garante que um novo item seja adicionado com os atributos corretos.
- **Atualizar Item (PUT /items/<id>)**: Valida a modificação de itens existentes.
- **Deletar Item (DELETE /items/<id>)**: Confirma que itens são deletados corretamente.


# Exemplo de JSON para Testes:

## Adicionar um Item Eletrônico:

{
  "nome": "notebook",
  "valor": 5000
}

## Adicionar um Item Não Eletrônico:

{
  "nome": "caneca",
  "valor": 18
}

# Resultados:

Os testes devem retornar um código de status 200 (OK) para as requisição.           
--- Home


![Workflow](https://github.com/arruda404/project-api/blob/main/img/inicial-img.png)





--- Get

![Workflow](https://github.com/arruda404/project-api/blob/main/img/get-img.png)


--- Update

![Workflow](https://github.com/arruda404/project-api/blob/main/img/put-img.png)


--- Delete

![Workflow](https://github.com/arruda404/project-api/blob/main/img/delete-img.png)

---Pytest 

![Workflow](https://github.com/arruda404/project-api/blob/main/img/pytester-img.png)
