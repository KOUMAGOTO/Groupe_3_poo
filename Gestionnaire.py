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
 
  def modif(self):
     print("veillez vous identifier pour modifier votre compte\n")
      iden = input("veuillez entrer votre id\n")
      cod = input(" veuillez entrer votre code\n")
      if (iden == self.user and cod == self.code1):
     print("Que vouliez vous modifier\n1- mon id\n2- mon mot de passe\n")
       n = input("\n")
       n = int(n)
       if n == 1:
     self.user = input("veuillez entrer votre nouveau id\n")
     print("id modifier avec sucess votre nouveau id est\n", self.id)
     elif n == 2:
     self.code1 = input("veuillez entrer votre nouveau mot de passe\n")
     self.code2 = input("veuillez confirmer votre nouveau mot de passe\n")
      while self.code1 != self.code2:
        print("les nouveuax mots de passe sont different veuiller reessayer\n")
         self.code1 = input("entrer votre nouveau mot de passe\n")
         self.code2 = input("confirmer votre nouveau mot de passe \n")
         print("votre mot de passe a ete modifier avec succes\nvotre nouveau mot de passe est:\n", self.code1)
         else:
             print("option non disponible") 
          else: 
            print("desole ce compte n'existe pas\n")  
  def suprim(self): #defini la fonction supprimer
      print(veuillez vous identifier pour supprimer votre compte\n")
      ide = input("entrer votre id\n")
      code = input("entrez votre mot de passe\n")
      if ide != self.id:
         Print("compte n'existe pas \n")
      elif code != self.code1:
         Print(" compte n'existe pas \n")
      else:
        sel.user = ""
        self.password1 = ""
        print("votre compte a ete supprime)


ab = Gestion ()
ab.ajout()
ab.modif()
ab.suprim()




