import os

from flask import render_template, send_from_directory

from app.controllers.cuidador_controller import CuidadorController
from app.controllers.guarderia_controller import GuarderiaController
from app.controllers.perro_controller import PerroController
from app.controllers.puntos_taller_controller import PuntosTallerController


def register_routes(app):
    @app.route("/")
    def home():
        return render_template("index.html")