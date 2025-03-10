import os

from flask import (flash, redirect, render_template, send_from_directory,
                   url_for)
from flask_login import current_user, login_required

from app.controllers.auth import auth
from app.controllers.cuidador_controller import CuidadorController
from app.controllers.guarderia_controller import GuarderiaController
from app.models.perro import Perro


def register_routes(app):
    @app.route("/")
    def home():
        return render_template("index.html")

    app.register_blueprint(auth, url_prefix="/auth")
    
    @app.route("/perros")
    @login_required
    def perros():
        if not current_user.is_admin:
            flash("No tienes permisos para acceder a esta página.", "danger")
            return redirect(url_for("home"))

        perros = Perro.query.all()
        perros_info = ""
        contador_perros = len(perros)

        for perro in perros:
            perros_info += f"<p>Este es <strong>{perro.nombre}</strong>!</p>"
            perros_info += f"<p>Es un hermosx <strong>{perro.raza}</strong>!</p>"
            perros_info += f"<p>Su edad es: <strong>{perro.edad}</strong> y pesa: <strong>{perro.peso}</strong></p><br>"

        return render_template("perros.html", perros_info=perros_info, contador_perros=contador_perros)