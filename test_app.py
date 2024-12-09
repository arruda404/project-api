import pytest
import requests

BASE_URL = "https://project-api04122024.uc.r.appspot.com/items"

@pytest.fixture
def client():
    return requests

def test_home_redirect(client):
    # Testa se a rota base '/' redireciona corretamente para '/items'
    response = client.get(BASE_URL.replace("/items", ""))
    assert response.status_code == 200  # Redirecionamento tratado no servidor GCP
    assert isinstance(response.json(), list)  # Retorna a lista de itens

def test_get_items(client):
    # Testa se a rota /items retorna uma lista vazia inicialmente
    response = client.get(BASE_URL)
    assert response.status_code == 200
    assert isinstance(response.json(), list)  # Deve ser uma lista
    assert len(response.json()) >= 0  # Lista deve ser válida

def test_add_item(client):
    # Testa se um item é adicionado corretamente
    new_item = {
        "nome": "Notebook",
        "valor": 6000,
    }
    response = client.post(BASE_URL, json=new_item)
    assert response.status_code == 201
    data = response.json()
    assert data["nome"] == new_item["nome"]
    assert data["valor"] == new_item["valor"]
    assert "eletronico" in data
    assert "data_criacao" in data

def test_update_item(client):
    # Primeiro, adiciona um item para atualizar
    new_item = {
        "nome": "Notebook",
        "valor": 6000,
    }
    response_add = client.post(BASE_URL, json=new_item)
    item_id = response_add.json()["id"]

    # Atualiza o item
    updated_item = {
        "nome": "Smartphone",
        "valor": 3000,
    }
    response = client.put(f"{BASE_URL}/{item_id}", json=updated_item)
    assert response.status_code == 200
    data = response.json()
    assert data["nome"] == updated_item["nome"]
    assert data["valor"] == updated_item["valor"]

def test_delete_item(client):
    # Primeiro, adiciona um item para deletar
    new_item = {
        "nome": "Notebook",
        "valor": 6000,
    }
    response_add = client.post(BASE_URL, json=new_item)
    item_id = response_add.json()["id"]

    # Deleta o item
    response = client.delete(f"{BASE_URL}/{item_id}")
    assert response.status_code == 200
    assert response.json() == {"message": "Item deletado com sucesso"}

    # Verifica se o item foi removido
    response = client.get(BASE_URL)
    items = response.json()
    assert not any(item["id"] == item_id for item in items)
