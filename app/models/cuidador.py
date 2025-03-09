from config.db import db


class Cuidador(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    nombre = db.Column(db.String(45), nullable=True)
    telefono = db.Column(db.String(15), nullable=True)
    id_guarderia = db.Column(db.Integer, nullable=True)
    
    def __init__(self, id: int, nombre: str, telefono: str, id_guarderia: int):
        self.__id = id
        self.__nombre = nombre
        self.__telefono = telefono
        self.__id_guarderia = id_guarderia
    
    def dar_informacion(self) -> str:
        return f"Nombre: {self.__nombre}, telefono: {self.__telefono}, ID guarderia: {self.__id_guarderia}."
    
    def get_id(self):
        return self.__id
    
    def get_nombre(self):
        return self.__nombre
    
    def get_telefono(self):
        return self.__telefono
    
    def get_id_guarderia(self):
        return self.__id_guarderia