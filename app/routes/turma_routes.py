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
            'examples': {'application/json': [{'id': 1, 'nome': 'Turma A', 'ano': 2025}]}
        }
    }
})
def listar_turmas():
    turmas = controller.listar_turmas()
    return jsonify([turma.to_dict() for turma in turmas])


@turma_bp.route('/turmas/<int:id>', methods=['GET'])
@swag_from({
    'tags': ['Turmas'],
    'summary': 'Buscar uma turma pelo ID',
    'parameters': [{'name': 'id', 'in': 'path', 'required': True, 'type': 'integer'}],
    'responses': {200: {'description': 'Turma encontrada'}, 404: {'description': 'Turma não encontrada'}}
})
def buscar_turma(id):
    turma = controller.buscar_turma(id)
    if turma:
        return jsonify(turma.to_dict())
    else:
        return jsonify({"erro": "Turma não encontrada"}), 404


@turma_bp.route('/turmas', methods=['POST'])
@swag_from({
    'tags': ['Turmas'],
    'summary': 'Criar uma nova turma',
    'parameters': [{
        'name': 'body',
        'in': 'body',
        'schema': {
            'type': 'object',
            'properties': {
                'nome': {'type': 'string'},
                'ano': {'type': 'integer'}
            },
            'required': ['nome', 'ano']
        }
    }],
    'responses': {201: {'description': 'Turma criada com sucesso'}}
})
def criar_turma():
    data = request.json
    nova = controller.criar_turma(data)
    if nova:
        return jsonify(nova.to_dict()), 201
    else:
        return jsonify({"erro": "Erro ao criar turma"}), 400


@turma_bp.route('/turmas/<int:id>', methods=['PUT'])
@swag_from({
    'tags': ['Turmas'],
    'summary': 'Atualizar uma turma pelo ID',
    'parameters': [
        {'name': 'id', 'in': 'path', 'required': True, 'type': 'integer'},
        {
            'name': 'body',
            'in': 'body',
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
    data = request.json
    turma = controller.atualizar_turma(id, data)
    if turma:
        return jsonify(turma.to_dict())
    else:
        return jsonify({"erro": "Turma não encontrada"}), 404


@turma_bp.route('/turmas/<int:id>', methods=['DELETE'])
@swag_from({
    'tags': ['Turmas'],
    'summary': 'Excluir uma turma pelo ID',
    'parameters': [{'name': 'id', 'in': 'path', 'required': True, 'type': 'integer'}],
    'responses': {
        200: {'description': 'Turma removida com sucesso'},
        404: {'description': 'Turma não encontrada'}
    }
})
def deletar_turma(id):
    sucesso = controller.deletar_turma(id)
    if sucesso:
        return jsonify({"mensagem": "Turma removida com sucesso"}), 200
    else:
        return jsonify({"erro": "Turma não encontrada"}), 404
