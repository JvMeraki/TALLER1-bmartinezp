from config.db import db


class Perro(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    nombre = db.Column(db.String(45), nullable=True)
    raza = db.Column(db.String(45), nullable=True)
    edad = db.Column(db.Integer, nullable=True)
    peso = db.Column(db.Numeric(precision=5, scale=2), nullable=True)
    id_guarderia = db.Column(db.Integer, nullable=True)
    id_cuidador = db.Column(db.Integer, nullable=True)
    
    def __init__(self, id: int, nombre: str, raza: str, peso: float, edad: int, id_guarderia: int, id_cuidador: int):
        self.__id = id
        self.__nombre = nombre
        self.__raza = raza
        self.__edad = edad
        self.__peso = peso
        self.__id_guarderia = id_guarderia
        self.__id_cuidador = id_cuidador
        
    def ladrar(self) -> str:
        return "guau guau"
    
    def modificar_peso(self, nuevo_peso) -> float:
        self.__peso = nuevo_peso
        
    def dar_nombre(self) -> str:
        return self.__nombre
    
    def dar_informacion(self) -> str:
        return f"Nombre: {self.__nombre}, Raza: {self.__raza}, Peso: {self.__peso} kg, Edad: {self.__edad} años."
    
    def get_id(self):
        return self.__id
    
    def get_nombre(self):
        return self.__nombre
    
    def get_raza(self):
        return self.__raza
    
    def get_peso(self):
        return self.__peso
    
    def get_edad(self):
        return self.__edad
    
    def get_id_guarderia(self):
        return self.__id_guarderia
    
    def get_id_cuidador(self):
        return self.__id_cuidador