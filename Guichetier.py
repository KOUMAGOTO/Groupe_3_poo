Gestionnaire.py
# Bemadji Arséne
#18A874FS
class Guichetier(PersonneBank):
    def __init__ (self, nom, solde=0, montant=0):
        self.montant = montant
        self.solde = 2000
    def IdeeSolde(self) :    
        print("votre solde est:\n", self.solde)
    def versement(self):
       montant=input("Saisir le montant à verser\n")
       montant=int(montant)
       self.solde += montant
       print("votre nouveau solde est:\n", self.solde)
    def retrait(self):
       somme = input("entrer le montant a retirer\n")
       somme = int(somme)
       if somme > self.solde:
          print("solde insuffisant")
       else:
          self.solde -= somme
          print("retrait de {} effectuer avec succes\n".format(somme))
          print("nouveau solde est:\n", self.solde) 
