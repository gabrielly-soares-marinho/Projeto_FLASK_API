from app import db
from app.models.aluno import Aluno

def listar_alunos():
    return Aluno.query.all()

def buscar_aluno(id):
    return Aluno.query.get(id)

def criar_aluno(data):
    try:
        aluno = Aluno(**data)
        db.session.add(aluno)
        db.session.commit()
        return aluno
    except Exception as e:
        db.session.rollback()
        print(f"Erro ao criar aluno: {e}")
        return None

def atualizar_aluno(id, data):
    aluno = Aluno.query.get(id)
    if not aluno:
        return None
    for key, value in data.items():
        setattr(aluno, key, value)
    try:
        db.session.commit()
        return aluno
    except Exception as e:
        db.session.rollback()
        print(f"Erro ao atualizar aluno: {e}")
        return None

def deletar_aluno(id):
    aluno = Aluno.query.get(id)
    if aluno:
        try:
            db.session.delete(aluno)
            db.session.commit()
            return True
        except Exception as e:
            db.session.rollback()
            print(f"Erro ao deletar aluno: {e}")
            return False
    else:
        return False
