from flask import make_response, render_template
from flask_restful import Resource

from app.models.guarderia import Guarderias


class GuarderiaController(Resource):
    def get(self):
        guarderias = Guarderias.query.all()
        guarderias_info = ""
        contador_guarderias = len(guarderias)
        for guarderia in guarderias:
            guarderias_info += f"<p>Esta es <strong>{guarderia.nombre}</strong>!</p>"
            guarderias_info += f"<p>Su telefóno es: <strong>{guarderia.telefono}</strong>!</p>"
            guarderias_info += f"<p>Y está ubicada en: <strong>{guarderia.direccion}</strong>!</p><br>"
        return make_response(render_template("guarderias.html", guarderias_info = guarderias_info, contador_guarderias = contador_guarderias))
