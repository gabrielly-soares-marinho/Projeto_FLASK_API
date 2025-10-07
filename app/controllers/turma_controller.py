from app import db
from app.models.turma import Turma

def listar_turmas():
    return Turma.query.all()

def buscar_turma(id):
    return Turma.query.get(id)

def criar_turma(data):
    try:
        turma = Turma(**data)
        db.session.add(turma)
        db.session.commit()
        return turma
    except Exception as e:
        db.session.rollback()
        print(f"Erro ao criar turma: {e}")
        return None

def atualizar_turma(id, data):
    turma = Turma.query.get(id)
    if not turma:
        return None
    for key, value in data.items():
        setattr(turma, key, value)
    try:
        db.session.commit()
        return turma
    except Exception as e:
        db.session.rollback()
        print(f"Erro ao atualizar turma: {e}")
        return None

def deletar_turma(id):
    turma = Turma.query.get(id)
    if turma:
        try:
            db.session.delete(turma)
            db.session.commit()
            return True
        except Exception as e:
            db.session.rollback()
            print(f"Erro ao deletar turma: {e}")
            return False
    return False
