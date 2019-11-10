# Mbaiondoum Ngonmiadje
# 17A513FS l2informatique
# NGABA PATRICE 18B235FS
# ALLARAMADJI MBAINDI GHISLAIN 18AFS191FS
Class Gestionnaire:
  def __init__(self):
     self.user = ""
     self.code1 = ""
     self.code2 = ""
  def ajout(self):
     self.user = input("Entrez votre nom svp\n")
     self.code1 = input("Entrez votre code\n")
     self.code2 = input("Confirmez votre code\n")
     while self.code1 != self.code2:
          print("Code incorrect, veuillez reesayer\n")
          self.code1 = input("Entrez votre code\n")
          self.code2 = input("Confirmez votre code\n")
     print("Votre compte est créé avec succès \n") 
