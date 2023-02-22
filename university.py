class university:
    # Creem el constructor amb els seus atributs
    def __init__(self, nom, numAlumnes, numClasses, m2, notaTall, numProfes):
        self.nom = nom
        self.autor = numAlumnes
        self.any = numClasses
        self.tapa = m2
        self.idioma = notaTall
        self.genere = numProfes

    # Afegim els Getters/Setters
    def getNom(self):
        return self.nom

    def setNom(self, nom):
        self.nom = nom

    def getNumAlumnes(self):
        return self.numAlumnes

    def setNumAlumnes(self, numAlumnes):
        self.numAlumnes = numAlumnes

    def getNumClasses(self):
        return self.numClasses

    def setNumClasses(self, numClasses):
        self.numClasses = numClasses

    def getM2(self):
        return self.m2

    def setM2(self, m2):
        self.m2 = m2

    def getNotaTall(self):
        return self.notaTall

    def setNotaTall(self, notaTall):
        self.notaTall = notaTall

    def getNumProfes(self):
        return self.numProfes

    def setNumProfes(self, numProfes):
        self.numProfes = numProfes

# Creem una funció que imprimeix els atributs de l'objecte per pantalla
    def info(self):
        print("L'universitat {nom} té places per {numAlumnes} alumnes amb un número total de {numClasses}"
              " classes. El centre té {m2} m2i és necessari un {notaTall} per entrar. El centre "
              "disposa de {numProfes} professors".format(nom=self.nom, numAlumnes=self.numAlumnes,
                numClasses=self.numClasses,m2=self.m2,notaTall=self.notaTall,numProfes=self.numProfes))