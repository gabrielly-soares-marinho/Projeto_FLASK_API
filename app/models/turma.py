from app import db

class Turma(db.Model):
    __tablename__ = 'turmas'
    id = db.Column(db.Integer, primary_key=True)
    descricao = db.Column(db.String(100))
    professor_id = db.Column(db.Integer, db.ForeignKey('professores.id'))
    ativo = db.Column(db.Boolean, default=True)

    alunos = db.relationship('Aluno', backref='turma', lazy=True)

    def to_dict(self):
        return {
            "id": self.id,
            "descricao": self.descricao,
            "professor_id": self.professor_id,
            "ativo": self.ativo
        }