class user:
    # Creem el constructor amb els seus atributs
    def __init__ (self, nom, edat, altura, pes, nacionalitat, genere):
        self.nom = nom
        self.autor = edat
        self.any = altura
        self.tapa = pes
        self.idioma = nacionalitat
        self.genere = genere

    # Afegim els Getters/Setters
    def getNom(self):
        return self.nom

    def setNom(self, nom):
        self.nom = nom

    def getEdat(self):
        return self.edat

    def setEdat(self, edat):
        self.edat = edat

    def getAltura(self):
        return self.altura

    def setAltura(self, altura):
        self.altura = altura

    def getPes(self):
        return self.pes

    def setPes(self, pes):
        self.pes = pes

    def getNacionalitat(self):
        return self.nacionalitat

    def setNacionalitat(self, nacionalitat):
        self.nacionalitat = nacionalitat

    def getGenere(self):
        return self.genere

    def setGenere(self, genere):
        self.genere = genere

    # Creem una funció que imprimeix els atributs de l'objecte per pantalla
    def salutacio(self):
        print("Em dic {nom} tinc {edat} medeixo {altura} cm, peso {pes},"
              " sóc {nacionalitat} i el meu gènere és {genere}".format(nom=self.nom, edat=self.edat,
                altura=self.altura,pes=self.pes,nacionalitat=self.nacionalitat,genere=self.genere))