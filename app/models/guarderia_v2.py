from config.db import db


class Guarderia(db.Model):
    __tablename__ = "guarderias"
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(45), nullable=True)
    direccion = db.Column(db.String(120), nullable=True)
    telefono = db.Column(db.String(15), nullable=True)
    
    def __repr__(self):
        return f"<Guarderia {self.nombre}>"
    
    def retornar_perros(self):
        """" Retorna todos los perros asociados a esta guardería (asumiendo que hay una relación)"""
        from models.perro import Perro
        return db.session.query(Perro).filter_by(guarderia_id=self.id).all()
    
    def dar_informacion(self) -> str:
        return f"Nombre: {self.nombre}, Dirección: {self.direccion}, Teléfono: {self.telefono}."