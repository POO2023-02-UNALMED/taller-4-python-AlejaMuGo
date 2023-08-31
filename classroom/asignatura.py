class Asignatura:

    def __init__(self, nombre=None, salon=None):
        self._nombre = nombre
        self._salon = salon

    def __str__(self):
        cadena = self._nombre + " remoto"
        return cadena
