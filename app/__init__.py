from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flasgger import Swagger

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)
    Swagger(app)

    from app.routes.professor_routes import professor_bp
    from app.routes.turma_routes import turma_bp
    from app.routes.aluno_routes import aluno_bp

    app.register_blueprint(professor_bp)
    app.register_blueprint(turma_bp)
    app.register_blueprint(aluno_bp)

    @app.route('/')
    def index():
        return """
        <h1>Bem-vindo à API de Gerenciamento Escolar!</h1>
        <ul>
            <li><a href='/apidocs'>Documentação Swagger</a></li>
        </ul>
        """

    return app