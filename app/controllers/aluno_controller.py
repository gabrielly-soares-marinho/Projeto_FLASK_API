from app import db
from app.models.aluno import Aluno

def listar_alunos():
    return Aluno.query.all()

def buscar_aluno(id):
    return Aluno.query.get(id)

def criar_aluno(data):
    aluno = Aluno(**data)
    db.session.add(aluno)
    db.session.commit()
    return aluno

def atualizar_aluno(id, data):
    aluno = Aluno.query.get(id)
    for key, value in data.items():
        setattr(aluno, key, value)
    db.session.commit()
    return aluno

def deletar_aluno(id):
    aluno = Aluno.query.get(id)
    db.session.delete(aluno)
    db.session.commit()