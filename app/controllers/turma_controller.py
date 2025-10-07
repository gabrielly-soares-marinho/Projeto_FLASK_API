from app import db
from app.models.turma import Turma

def listar_turmas():
    return Turma.query.all()

def buscar_turma(id):
    return Turma.query.get(id)

def criar_turma(data):
    turma = Turma(**data)
    db.session.add(turma)
    db.session.commit()
    return turma

def atualizar_turma(id, data):
    turma = Turma.query.get(id)
    for key, value in data.items():
        setattr(turma, key, value)
    db.session.commit()
    return turma

def deletar_turma(id):
    turma = Turma.query.get(id)
    db.session.delete(turma)
    db.session.commit()
