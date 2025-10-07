from app import db

class Turma(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    ano = db.Column(db.Integer, nullable=False)  # campo ano adicionado

    def to_dict(self):
        return {
            'id': self.id,
            'nome': self.nome,
            'ano': self.ano
        }
