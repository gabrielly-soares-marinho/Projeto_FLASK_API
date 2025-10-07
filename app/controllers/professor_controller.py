from app import db
from app.models.professor import Professor

def listar_professores():
    return Professor.query.all()

def buscar_professor(id):
    return Professor.query.get(id)

def criar_professor(data):
    try:
        professor = Professor(**data)
        db.session.add(professor)
        db.session.commit()
        return professor
    except Exception as e:
        db.session.rollback()
        print(f"Erro ao criar professor: {e}")
        return None

def atualizar_professor(id, data):
    professor = Professor.query.get(id)
    if not professor:
        return None
    for key, value in data.items():
        setattr(professor, key, value)
    try:
        db.session.commit()
        return professor
    except Exception as e:
        db.session.rollback()
        print(f"Erro ao atualizar professor: {e}")
        return None

def deletar_professor(id):
    professor = Professor.query.get(id)
    if professor:
        try:
            db.session.delete(professor)
            db.session.commit()
            return True
        except Exception as e:
            db.session.rollback()
            print(f"Erro ao deletar professor: {e}")
            return False
    return False
