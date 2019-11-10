
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
