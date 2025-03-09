from flask import make_response, render_template
from flask_restful import Resource

from app.models.cuidador import Cuidador


class CuidadorController(Resource):
    def get(self):
        cuidadores = Cuidador.query.all()
        cuidadores_info = ""
        contador_cuidadores = len(cuidadores)
        for cuidador in cuidadores:
            cuidadores_info += f"<p>Este es <strong>{cuidador.nombre}</strong>!</p>"
            cuidadores_info += f"<p>Su telefóno es: <strong>{cuidador.telefono}</strong>!</p><br>"
        return make_response(render_template("cuidadores.html", cuidadores_info = cuidadores_info, contador_cuidadores = contador_cuidadores))
