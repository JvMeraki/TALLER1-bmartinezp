from flask import make_response, render_template
from flask_restful import Resource

from app.models.perro import Perro


class PerroController(Resource):
    def get(self):
        perros = Perro.query.all()
        perros_info = ""
        contador_perros = len(perros)
        for perro in perros:
            perros_info += f"<p>Este es <strong>{perro.nombre}</strong>!</p>"
            perros_info += f"<p>Es un hermosx <strong>{perro.raza}</strong>!</p>"
            perros_info += f"<p>Su edad es: <strong>{perro.edad}</strong> y pesa: <strong>{perro.peso}</strong></p><br>"
        return make_response(render_template("perros.html", perros_info = perros_info, contador_perros = contador_perros))
