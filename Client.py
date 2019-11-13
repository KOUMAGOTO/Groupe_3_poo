Issa rouzoumka yadia 18A919FS

classe Client:
   def __init __ (self, numero):
      self.numero = numero
      self.solde = 10000
   def InfoSolde(self):
       print("votre solde est:\n", self.solde)
   def versement(self):
       som = input("combien vouliez vous verser ?\n")
       som = int(som)
       self.solde += som
       print("votre nouveau solde est:\n", self.solde)
   def retrait(self):
       somme = input("entrer le montant a retirer\n")
       somme = int(somme)
       if somme > self.solde:
          print("solde insuffisant")
       else:
          self.solde - = somme
          print ("retrait de {} effectuer avec succes \ n" .form (somme))
          print("nouveau solde est:\n", self.solde)
Issa = Client(12)
Issa.InfoSolde()
Issa.versement()
Issa.retrait()
Issa.retrait()
Issa.retrait()
Issa.versement ():
