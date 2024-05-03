class Herr():
    
    def __init__(self,id,nombre=None, precio=None) -> None:
        self.id= id
        self.nombre= nombre
        self.precio= precio
        
def to_JSON(self):
    return {
        'id': self.id,
        'nombre': self.nombre,
        'precio': self.precio
    }