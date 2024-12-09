
# API de Gerenciamento de Itens

## Descrição
Esta aplicação é uma API desenvolvida em Flask para gerenciar itens com deploy no Google Cloud Platform.  
Ela permite listar, adicionar, atualizar e excluir itens, com atributos específicos, como nome, valor, data de criação e a identificação de itens eletrônicos.

---

**Foi realizado um parâmetro para identificar automaticamente se o item é eletrônico (`true`) ou não (`false`).**

---

### Incrementações Futuras:
- Implementação de **Inteligência Artificial** para verificar automaticamente quando o item é eletrônico.
- Integração com um banco de dados para armazenamento persistente dos itens e contagem de itens iguais.

---

## Funcionalidades
A API oferece os seguintes endpoints:
- **`GET /items`** - Listar todos os itens.
- **`POST /items`** - Adicionar um novo item.
- **`PUT /items/<id>`** - Atualizar um item existente.
- **`DELETE /items/<id>`** - Deletar um item existente.

---

## Configuração e Instalação

### Requisitos Locais
- **Python** 3.12 ou superior.
- **Bibliotecas Python**:
  - Flask
  - Pytest (para testes).

---

### Passos para Implantação Local

1. **Clone o repositório:**
   ```bash
   git clone <url do repositorio>
   cd <para onde foi copiado o arquivo>

2. **Crie e ative o ambiente virtual:**
  python -m venv venv
  source venv/bin/activate  # No Windows: venv\\Scripts\\activate

3. **Instale as dependências:**
  pip install -r requirements.txt

4. **Execute a aplicação localmente:**
  python app.py

5. **Acesse a API no navegador ou Postman:**
  URL local: http://127.0.0.1:5000/items.

---
## Implantação no Google Cloud Platform (GCP)
 - Pré-requisitos
 - Conta no Google Cloud Platform.
 - Ativação do projeto GCP.
 - Cloud SDK instalado localmente.
 - App Engine habilitado no GCP.


**Passos**
  1. Autenticação no GCP:
  gcloud auth login
  
  2. Selecione o projeto GCP:
  gcloud config set project <SEU_ID_DO_PROJETO>

  3. Prepare o ambiente para App Engine:
  gcloud app create --region=<REGIAO>

  4. Adicione o arquivo app.yaml: Crie o arquivo app.yaml na raiz do projeto:
  runtime: python310
  entrypoint: python app.py
  env: standard

 5. Instale as dependências localmente para GCP: requirements.txt:
  flask
  requests
  pytest

 6. Realize o deploy da aplicação:
  gcloud app deploy
  
7. Acesse a URL fornecida pelo GCP: Após o deploy, você verá uma mensagem com a URL da aplicação:
  Deployed service [default] to [https://<SEU_PROJETO>.uc.r.appspot.com]
---

## Testes Automatizados
**Executar Testes Locais**
 1. Instale o Pytest:
    pip install pytest

 2. Execute os testes:
   pytest -vv

**Executar Testes no GCP**
Atualize o arquivo test_app.py para utilizar o Base URL do GCP: 
  BASE_URL = "https://<SEU_PROJETO>.uc.r.appspot.com/items"
  Execute os testes:
  pytest test_app.py

## Exemplo de JSON para Testes
**Adicionar um Item Eletrônico:**

{
  "nome": "notebook",
  "valor": 5000
}

**Adicionar um Item Não Eletrônico:**

{
  "nome": "caneca",
  "valor": 18
}



## Resultados dos Testes
  Os testes devem retornar um código de status 200 (OK) para todas as requisições válidas.
  Abaixo, estão os resultados esperados:



Adicionar: Item adicionado corretamente e listados no formato JSON.

![Workflow](https://github.com/arruda404/project-api/blob/main/img/get-img.png)


Atualizar: Item atualizado com sucesso.

![Workflow](https://github.com/arruda404/project-api/blob/main/img/put-img.png)


Deletar: Item removido corretamente.

![Workflow](https://github.com/arruda404/project-api/blob/main/img/delete-img.png)

Teste Pytest.

![Workflow](https://github.com/arruda404/project-api/blob/main/img/pytester-img.png)
