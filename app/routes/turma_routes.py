from flask import Blueprint, request, jsonify
from app.controllers import turma_controller as controller
from flasgger import swag_from

turma_bp = Blueprint('turmas', __name__)

@turma_bp.route('/turmas', methods=['GET'])
@swag_from({
    'tags': ['Turmas'],
    'summary': 'Listar todas as turmas',
    'responses': {
        200: {
            'description': 'Lista de turmas',
            'examples': {
                'application/json': [
                    {'id': 1, 'nome': 'Turma A', 'ano': 2025}
                ]
            }
        }
    }
})
def listar_turmas():
    return jsonify(controller.listar_turmas())

@turma_bp.route('/turmas/<int:id>', methods=['GET'])
@swag_from({
    'tags': ['Turmas'],
    'summary': 'Buscar uma turma pelo ID',
    'parameters': [
        {'name': 'id', 'in': 'path', 'required': True, 'type': 'integer'}
    ],
    'responses': {
        200: {'description': 'Turma encontrada'},
        404: {'description': 'Turma não encontrada'}
    }
})
def buscar_turma(id):
    turma = controller.buscar_turma(id)
    if turma:
        return jsonify(turma.__dict__)
    return jsonify({"erro": "Turma não encontrada"}), 404

@turma_bp.route('/turmas', methods=['POST'])
@swag_from({
    'tags': ['Turmas'],
    'summary': 'Criar uma nova turma',
    'parameters': [
        {
            'name': 'body',
            'in': 'body',
            'required': True,
            'schema': {
                'type': 'object',
                'properties': {
                    'nome': {'type': 'string'},
                    'ano': {'type': 'integer'}
                },
                'required': ['nome', 'ano']
            }
        }
    ],
    'responses': {
        201: {'description': 'Turma criada com sucesso'},
        400: {'description': 'Dados inválidos'}
    }
})
def criar_turma():
    data = request.get_json()
    nova = controller.criar_turma(data)
    return jsonify(nova.__dict__), 201

@turma_bp.route('/turmas/<int:id>', methods=['PUT'])
@swag_from({
    'tags': ['Turmas'],
    'summary': 'Atualizar uma turma pelo ID',
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
                    'ano': {'type': 'integer'}
                }
            }
        }
    ],
    'responses': {
        200: {'description': 'Turma atualizada com sucesso'},
        404: {'description': 'Turma não encontrada'}
    }
})
def atualizar_turma(id):
    data = request.get_json()
    turma = controller.atualizar_turma(id, data)
    if turma:
        return jsonify(turma.__dict__)
    return jsonify({"erro": "Turma não encontrada"}), 404

@turma_bp.route('/turmas/<int:id>', methods=['DELETE'])
@swag_from({
    'tags': ['Turmas'],
    'summary': 'Excluir uma turma pelo ID',
    'parameters': [
        {'name': 'id', 'in': 'path', 'required': True, 'type': 'integer'}
    ],
    'responses': {
        200: {'description': 'Turma removida com sucesso'},
        404: {'description': 'Turma não encontrada'}
    }
})
def deletar_turma(id):
    turma = controller.deletar_turma(id)
    if turma:
        return jsonify({"mensagem": "Turma removida com sucesso"})
    return jsonify({"erro": "Turma não encontrada"}), 404
