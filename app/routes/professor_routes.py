from flask import Blueprint, request, jsonify
from app.controllers import professor_controller as controller
from flasgger import swag_from

professor_bp = Blueprint('professores', __name__)

@professor_bp.route('/professores', methods=['GET'])
@swag_from({
    'tags': ['Professores'],
    'summary': 'Listar todos os professores',
    'responses': {
        200: {
            'description': 'Lista de professores',
            'examples': {'application/json': [{'id': 1, 'nome': 'Carlos Silva', 'disciplina': 'Matemática'}]}
        }
    }
})
def listar_professores():
    professores = controller.listar_professores()
    return jsonify([prof.to_dict() for prof in professores])


@professor_bp.route('/professores/<int:id>', methods=['GET'])
@swag_from({
    'tags': ['Professores'],
    'summary': 'Buscar um professor pelo ID',
    'parameters': [{'name': 'id', 'in': 'path', 'required': True, 'type': 'integer'}],
    'responses': {200: {'description': 'Professor encontrado'}, 404: {'description': 'Professor não encontrado'}}
})
def buscar_professor(id):
    prof = controller.buscar_professor(id)
    if prof:
        return jsonify(prof.to_dict())
    else:
        return jsonify({"erro": "Professor não encontrado"}), 404


@professor_bp.route('/professores', methods=['POST'])
@swag_from({
    'tags': ['Professores'],
    'summary': 'Criar um novo professor',
    'parameters': [{
        'name': 'body',
        'in': 'body',
        'schema': {
            'type': 'object',
            'properties': {
                'nome': {'type': 'string'},
                'disciplina': {'type': 'string'}
            },
            'required': ['nome', 'disciplina']
        }
    }],
    'responses': {201: {'description': 'Professor criado com sucesso'}}
})
def criar_professor():
    data = request.json
    novo = controller.criar_professor(data)
    if novo:
        return jsonify(novo.to_dict()), 201
    else:
        return jsonify({"erro": "Erro ao criar professor"}), 400


@professor_bp.route('/professores/<int:id>', methods=['PUT'])
@swag_from({
    'tags': ['Professores'],
    'summary': 'Atualizar um professor pelo ID',
    'parameters': [
        {'name': 'id', 'in': 'path', 'required': True, 'type': 'integer'},
        {
            'name': 'body',
            'in': 'body',
            'schema': {
                'type': 'object',
                'properties': {
                    'nome': {'type': 'string'},
                    'disciplina': {'type': 'string'}
                }
            }
        }
    ],
    'responses': {
        200: {'description': 'Professor atualizado com sucesso'},
        404: {'description': 'Professor não encontrado'}
    }
})
def atualizar_professor(id):
    data = request.json
    prof = controller.atualizar_professor(id, data)
    if prof:
        return jsonify(prof.to_dict())
    else:
        return jsonify({"erro": "Professor não encontrado"}), 404


@professor_bp.route('/professores/<int:id>', methods=['DELETE'])
@swag_from({
    'tags': ['Professores'],
    'summary': 'Excluir um professor pelo ID',
    'parameters': [{'name': 'id', 'in': 'path', 'required': True, 'type': 'integer'}],
    'responses': {
        200: {'description': 'Professor removido com sucesso'},
        404: {'description': 'Professor não encontrado'}
    }
})
def deletar_professor(id):
    sucesso = controller.deletar_professor(id)
    if sucesso:
        return jsonify({"mensagem": "Professor removido com sucesso"}), 200
    else:
        return jsonify({"erro": "Professor não encontrado"}), 404
