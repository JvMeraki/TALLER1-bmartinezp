from app.config.db import db


class Guarderias(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    nombre = db.Column(db.String(45), nullable=True)
    direccion = db.Column(db.String(120), nullable=True)
    telefono = db.Column(db.String(15), nullable=True)
    
    def __init__(self, id: int, nombre: str, direccion: str, telefono: str):
        self.__id = id
        self.__nombre = nombre
        self.__direccion = direccion
        self.__telefono = telefono
    
    def retornar_perros(self):
        tupla_perros = (db.query.all())
        return tupla_perros
    
    def dar_informacion(self) -> str:
        return f"Nombre: {self.__nombre}, Direccion: {self.__direccion}, telefono: {self.__telefono}."
    
    def get_id(self):
        return self.__id
    
    def get_nombre(self):
        return self.__nombre
    
    def get_direccion(self):
        return self.__direccion
    
    def get_telefono(self):
        return self.__telefono