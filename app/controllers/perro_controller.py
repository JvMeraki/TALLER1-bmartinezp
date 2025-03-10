from flask import flash, make_response, redirect, render_template, url_for
from flask_login import current_user, login_required
from flask_restful import Resource

from app.models.perro import Perro


class PerroController(Resource):
    @login_required
    def get(self):
        # Redirigir si el usuario no es administrador
        if not current_user.is_admin:
            flash("No tienes permisos para acceder a esta página.", "danger")
            print("Redirigiendo a home porque el usuario no es admin")  # Depuración
            return redirect(url_for("home"))

        print("Usuario admin, obteniendo perros de la base de datos...")  # Depuración

        perros = Perro.query.all()
        print(f"Perros obtenidos: {perros}")  # Verifica si realmente obtiene los datos

        perros_info = ""
        contador_perros = len(perros)

        for perro in perros:
            print(f"Procesando perro: {perro.nombre}, {perro.raza}, {perro.edad}, {perro.peso}")  # Depuración
            perros_info += f"<p>Este es <strong>{perro.nombre}</strong>!</p>"
            perros_info += f"<p>Es un hermosx <strong>{perro.raza}</strong>!</p>"
            perros_info += f"<p>Su edad es: <strong>{perro.edad}</strong> y pesa: <strong>{perro.peso}</strong></p><br>"

        return make_response(render_template("perros.html", perros_info=perros_info, contador_perros=contador_perros))