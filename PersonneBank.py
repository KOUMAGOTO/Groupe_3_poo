# KOUMAGOTO Mboîtam Patrick
#Matricule:18A180Fs

class PersonneBank:  # création de la super classe
    def __init__(self,nom = "",prenom = ""):
        self.nom = nom
        self.prenom = prenom

    def __str__(self):
        return "nom :" + self._nom + "\prenom:" +self._prenom

    def _get_nom(self):
        return self._nom
    def _set_nom(self,n):
        self._nom = n
    nom = property(_get_nom,_set_nom)

    def _get_prenom(self):
        return self._prenom
    def _set_prenom(self,n):
        self._prenom = p
    nom = property(_get_prenom,_set_prenom)
    def afficher(self):
        self.nom = input("veillez entrer votre nom\n")
        self.prenom=input("veillez entrer votre prenom\n")
        print(“votre nom, prénom est = “)
