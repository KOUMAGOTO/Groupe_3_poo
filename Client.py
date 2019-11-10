
Classe Client: 
def init (self, numero): 
self.numero = numero 
self.solde = 10000 
def InfoSolde (self): 
impression ("votre solde est: \ n", self.solde) 
def renvoi ( self): 
som = input ("combien vouliez vous verser? \ n") 
som = int (som) 
self.solde + = som 
print ("votre nouveau solde: \ n", self.solde) 
def retrait (self) : 
somme = input ("entrer le montant à retirer \ n") 
somme = int (somme) 
si somme> self.solde: 
print ("solde insuffisant") 
else: 
self.solde - = somme 
print ("retrait de {} effectuer avec succes \ n ".format (somme))
print ("nouveau solde est: \ n", self.solde) 
issa = Client (12) 
issa.InfoSolde () 
issa.versement () 
issa.retrait () 
issa.retrait () 
issa.retrait () 
issa.versement () )

