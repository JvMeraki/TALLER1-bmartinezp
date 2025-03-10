from flask import Flask
from flask_login import LoginManager
from flask_restful import Api

from app.config.config import Config
from app.config.db import db
from app.config.routes import register_routes
from app.controllers.cuidador_controller import CuidadorController
from app.controllers.guarderia_controller import GuarderiaController
from app.controllers.perro_controller import PerroController
from app.controllers.puntos_taller_controller import PuntosTallerController

login_manager = LoginManager()
login_manager.login_view = "auth.login"

def create_app(config_app=Config):
    app = Flask(__name__, template_folder="views", static_folder="static")
    
    app.config.from_object(config_app)
    db.init_app(app)
    login_manager.init_app(app)
    api = Api(app)
    register_routes(app)

    api.add_resource(PerroController, '/perros')
    api.add_resource(CuidadorController, '/cuidadores')
    api.add_resource(GuarderiaController, '/guarderias')
    api.add_resource(PuntosTallerController, '/puntos_taller', endpoint='puntos_taller')

    with app.app_context():
        db.create_all()

    return app

@login_manager.user_loader
def load_user(user_id):
    from app.models.user import User
    return User.query.get(int(user_id))