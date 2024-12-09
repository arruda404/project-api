from flask import Flask, request, jsonify, redirect
from datetime import datetime

app = Flask(__name__)

# Lista para armazenar os itens
items = []

# Rota principal com redirecionamento para /items
@app.route('/')
def api_home():
    return redirect('/items')

# Rota para listar todos os itens
@app.route('/items', methods=['GET'])
def get_items():
    return jsonify(items), 200

# Rota para adicionar um novo item
@app.route('/items', methods=['POST'])
def add_item():
    data = request.json

    # Lista de palavras-chave para identificar itens eletrônicos
    eletronic_keywords = [
        "computador", "notebook", "celular", "smartphone", "tablet", "televisão", 
        "monitor", "fones", "câmera", "tv", "ipad", "desktop", "mouse", "tela", 
        "smartwatch", "fones de ouvido", "console de videogame", "impressora", 
        "scanner", "câmera fotográfica", "projetor", "roteador Wi-Fi", 
        "disco rígido externo", "pendrive", "carregador", "processador", 
        "placa de vídeo", "placa-mãe", "teclado", "monitor curvo"
    ]
    nome = data.get('nome', '').lower()

    # Determinar se é eletrônico
    is_eletronico = any(keyword in nome for keyword in eletronic_keywords)

    # Formatando a data no formato solicitado
    now = datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%S')

    # Criando o novo item
    new_item = {
        'id': len(items) + 1,
        'nome': data['nome'],
        'valor': data['valor'],
        'eletronico': is_eletronico,
        'data_criacao': now
    }
    items.append(new_item)
    return jsonify(new_item), 201

# Rota para alterar um item existente
@app.route('/items/<int:item_id>', methods=['PUT'])
def update_item(item_id):
    data = request.json
    item = next((item for item in items if item['id'] == item_id), None)

    if not item:
        return jsonify({'message': 'Item não encontrado'}), 404

    # Atualizando os campos do item
    item['nome'] = data.get('nome', item['nome'])
    item['valor'] = data.get('valor', item['valor'])

    # Atualizar se é eletrônico com base no nome
    eletronic_keywords = [
        "computador", "notebook", "celular", "smartphone", "tablet", "televisão", 
        "monitor", "fones", "câmera", "tv", "ipad", "desktop", "mouse", "tela", 
        "smartwatch", "fones de ouvido", "console de videogame", "impressora", 
        "scanner", "câmera fotográfica", "projetor", "roteador Wi-Fi", 
        "disco rígido externo", "pendrive", "carregador", "processador", 
        "placa de vídeo", "placa-mãe", "teclado", "monitor curvo"
    ]
    nome = item['nome'].lower()
    item['eletronico'] = any(keyword in nome for keyword in eletronic_keywords)

    return jsonify(item), 200

# Rota para deletar um item existente
@app.route('/items/<int:item_id>', methods=['DELETE'])
def delete_item(item_id):
    global items
    items = [item for item in items if item['id'] != item_id]
    return jsonify({'message': 'Item deletado com sucesso'}), 200

if __name__ == '__main__':
    app.run(debug=True)
