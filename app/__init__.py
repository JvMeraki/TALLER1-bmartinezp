from config.config import Config
from config.db import db
from controllers.cuidador_controller import CuidadorController
from controllers.guarderia_controller import GuarderiaController
from controllers.perro_controller import PerroController
from controllers.puntos_taller_controller import PuntosTallerController
from flask import Flask, make_response, render_template
from flask_restful import Api

app = Flask(__name__, template_folder="views")
app.config.from_object(Config)
db.init_app(app)
api = Api(app)

@app.route("/")
def home():
    return render_template("index.html")
    
api.add_resource(PerroController, '/perros')
api.add_resource(CuidadorController, '/cuidadores')
api.add_resource(GuarderiaController, '/guarderias')
api.add_resource(PuntosTallerController, '/puntos_taller', endpoint='puntos_taller')

if __name__ == "__main__":
    app.run(debug=True)