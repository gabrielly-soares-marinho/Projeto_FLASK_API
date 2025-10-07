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
            'examples': {
                'application/json': [
                    {'id': 1, 'nome': 'Carlos Silva', 'disciplina': 'Matemática'}
                ]
            }
        }
    }
})
def listar_professores():
    return jsonify(controller.listar_professores())

@professor_bp.route('/professores/<int:id>', methods=['GET'])
@swag_from({
    'tags': ['Professores'],
    'summary': 'Buscar um professor pelo ID',
    'parameters': [
        {'name': 'id', 'in': 'path', 'required': True, 'type': 'integer'}
    ],
    'responses': {
        200: {'description': 'Professor encontrado'},
        404: {'description': 'Professor não encontrado'}
    }
})
def buscar_professor(id):
    professor = controller.buscar_professor(id)
    if professor:
        return jsonify(professor.__dict__)
    return jsonify({"erro": "Professor não encontrado"}), 404

@professor_bp.route('/professores', methods=['POST'])
@swag_from({
    'tags': ['Professores'],
    'summary': 'Criar um novo professor',
    'parameters': [
        {
            'name': 'body',
            'in': 'body',
            'required': True,
            'schema': {
                'type': 'object',
                'properties': {
                    'nome': {'type': 'string'},
                    'disciplina': {'type': 'string'}
                },
                'required': ['nome', 'disciplina']
            }
        }
    ],
    'responses': {
        201: {'description': 'Professor criado com sucesso'},
        400: {'description': 'Dados inválidos'}
    }
})
def criar_professor():
    data = request.get_json()
    novo = controller.criar_professor(data)
    return jsonify(novo.__dict__), 201

@professor_bp.route('/professores/<int:id>', methods=['PUT'])
@swag_from({
    'tags': ['Professores'],
    'summary': 'Atualizar um professor pelo ID',
    'parameters': [
        {'name': 'id', 'in': 'path', 'required': True, 'type': 'integer'},
        {
            'name': 'body',
            'in': 'body',
            'required': True,
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
    data = request.get_json()
    professor = controller.atualizar_professor(id, data)
    if professor:
        return jsonify(professor.__dict__)
    return jsonify({"erro": "Professor não encontrado"}), 404

@professor_bp.route('/professores/<int:id>', methods=['DELETE'])
@swag_from({
    'tags': ['Professores'],
    'summary': 'Excluir um professor pelo ID',
    'parameters': [
        {'name': 'id', 'in': 'path', 'required': True, 'type': 'integer'}
    ],
    'responses': {
        200: {'description': 'Professor removido com sucesso'},
        404: {'description': 'Professor não encontrado'}
    }
})
def deletar_professor(id):
    professor = controller.deletar_professor(id)
    if professor:
        return jsonify({"mensagem": "Professor removido com sucesso"})
    return jsonify({"erro": "Professor não encontrado"}), 404