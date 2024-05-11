class Herr:
    
    def __init__(self, id, nombre=None, precio=None, precioInternacional=None):
        self.id = id
        self.nombre = nombre
        self.precio = precio
        self.precioInternacional = precioInternacional
        
        
    def to_JSON(self):
        return {
            'id': self.id,
            'nombre': self.nombre,
            'precio': self.precio,
            'precioInternacional': self.precioInternacional,
            
        }