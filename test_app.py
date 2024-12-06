import pytest
from app import app  # Substitua 'app' pelo nome correto do seu módulo Flask

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_home(client):
    response = client.get("/")
    assert response.status_code == 200
    assert response.get_json() == {
        'message': 'API de gerenciamento de itens!',
        'endpoints': {
            'GET /items': 'Listar  itens.',
            'POST /items': 'Adicionar um novo item.',
            'PUT /items/<id>': 'Alterar um item existente.',
            'DELETE /items/<id>': 'Deletar um item existente.'
        },
        
    }

def test_add_item(client):
    new_item = {
        "nome": "Notebook",
        "valor": 6000,
        
    }
    response = client.post("/items", json=new_item)
    assert response.status_code == 201
    data = response.get_json()
    assert data["nome"] == new_item["nome"]
    assert data["valor"] == new_item["valor"]
      

def test_update_item(client):
    updated_item = {
        "nome": "Smartphone",
        "valor": 3000,
        
    }
    response = client.put("/items/1", json=updated_item)
    assert response.status_code == 200
    data = response.get_json()
    assert data["nome"] == updated_item["nome"]
    assert data["valor"] == updated_item["valor"]
    

def test_delete_item(client):
    response = client.delete("/items/1")
    assert response.status_code == 200
    assert response.get_json() == {"message": "Item deletado com sucesso"}
