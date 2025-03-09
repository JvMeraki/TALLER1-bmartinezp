from config.db import db
from flask import make_response, redirect, render_template, request, url_for
from flask_restful import Resource
from models.cuidador import Cuidador
from models.guarderia import Guarderias
from models.perro import Perro


class PuntosTallerController(Resource): 
    def get(self):
        # Obtener la información de Lassie
        lassies = db.session.query(
            Perro.id, Perro.nombre, Guarderias.nombre.label("guarderia"), Cuidador.nombre.label("cuidador")
        ).join(Guarderias, Perro.id_guarderia == Guarderias.id)\
         .join(Cuidador, Perro.id_cuidador == Cuidador.id)\
         .filter(Perro.nombre == "Lassie").all()

        # Obtener el ID de Mario
        mario = db.session.query(Cuidador.id).filter(Cuidador.nombre.ilike("mario")).first()
        id_mario = mario.id if mario else None

        # Obtener el ID de la guardería "La Favorita"
        favorita = db.session.query(Guarderias.id).filter(Guarderias.nombre.ilike("la favorita")).first()
        id_favorita = favorita.id if favorita else None

        # Verificar si existen antes de realizar la consulta
        if id_mario is not None:
            perros_mario = db.session.query(
                Perro.id, Perro.nombre, Perro.peso, Guarderias.nombre.label("guarderia")
            ).join(Guarderias, Perro.id_guarderia == Guarderias.id)\
             .filter(Perro.peso < 3, Perro.id_cuidador == id_mario).all()
        else:
            perros_mario = []  # Si Mario no existe, devolver lista vacía

        return make_response(render_template("index.html", lassies=lassies, perros_mario=perros_mario))

    def post(self):
        # Obtener el ID de Mario y de "La Favorita"
        mario = db.session.query(Cuidador.id).filter(Cuidador.nombre.ilike("mario")).first()
        id_mario = mario.id if mario else None

        favorita = db.session.query(Guarderias.id).filter(Guarderias.nombre.ilike("la favorita")).first()
        id_favorita = favorita.id if favorita else None

        if id_mario is not None and id_favorita is not None:
            db.session.query(Perro).filter(
                Perro.peso < 3, Perro.id_guarderia == id_favorita
            ).update({"id_cuidador": id_mario})

            db.session.commit()

        return redirect(url_for("puntos_taller"))  # Recargar página