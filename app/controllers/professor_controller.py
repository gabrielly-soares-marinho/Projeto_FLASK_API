from app import db
from app.models.professor import Professor

def listar_professores():
    return Professor.query.all()

def buscar_professor(id):
    return Professor.query.get(id)

def criar_professor(data):
    professor = Professor(**data)
    db.session.add(professor)
    db.session.commit()
    return professor

def atualizar_professor(id, data):
    professor = Professor.query.get(id)
    for key, value in data.items():
        setattr(professor, key, value)
    db.session.commit()
    return professor

def deletar_professor(id):
    professor = Professor.query.get(id)
    db.session.delete(professor)
    db.session.commit()