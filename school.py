# Classe School
class school:
    def __init__(self, nombre, tipo, direccion, telefono, nAlumnos, nProfes):
        self.nombre = nombre
        self.tipo = tipo
        self.direccion = direccion
        self.telefono = telefono
        self.nAlumnos = nAlumnos
        self.nProfes = nProfes

    # Getters y Setters
    def getNombre(self):
        return self.nombre

    def setNombre(self, nombre):
        self.nombre = nombre

    def getTipo(self):
        return self.tipo

    def setTipo(self, tipo):
        self.tipo = tipo

    def getDireccion(self):
        return self.direccion

    def setDireccion(self, direccion):
        self.direccion = direccion

    def getTelefono(self):
        return self.telefono

    def setTelefono(self, telefono):
        self.telefono = telefono

    def getNAlumnos(self):
        return self.nAlumnos

    def setNAlumnos(self, nAlumnos):
        self.nAlumnos = nAlumnos

    def getNProfes(self):
        return self.nProfes

    def setNProfes(self, nProfes):
        self.nProfes = nProfes

    # Imprime todos los attributos por la pantalla
    def info(self):
        print(
            "la escuela se llama {nombre}, es una escuela {tipo} que esta situado en {direccion} con numero de telefono {telefono}, tiene en total {nAlumnos} alumnos y {nProfes} profesores"
            .format(nombre=self.nombre, tipo=self.tipo, direccion=self.direccion, telefono=self.telefono,
                    nAlumnos=self.nAlumnos, nProfes=self.nProfes))
