
# Bemadji Arséne
#18A874FS
# KODJIYANOUBA CHRISTIANE
#18A998FS
class Guichetier(PersonneBank):
  def __init__(self):
      self.sold = 9000
  def solde(self):
      print("solde disponible est de {0} fcfa ".format(self.sold))
  def versement(self, montant):
      self.sold += montant
      print("versement de {} fcfa".format(montant))
      self.solde()
        
  def retrait(self):
      som = input("entrer le montant a retirer\n")
      som = int(som)
      if som <= self.sold:
          print("vous avez effectuer un retrait de ", som)
      else:
          print("solde insuffisant pour faire le retrait")
def retrait(self):
    som=input("entrer le montant à retirer\n")
    som=int(som)
    if som<=self.solde:
        print("vous avez effectué un retrait de", som)
    else:
        print("solde insuffisant pour faire le retrait")
def virement(self, montant):
   self.retrait(self)
   montant.versement(self)
   print("le virement a ete effectuer")
abo = Guichetier()
abo.retrait()
abo.versement(5500)
abo.virement(2000)
