# -*- coding: utf-8 -*-
"""
Created on Mon Nov 09 08:57:03 2019

@author: KODJIYANOUBA CHRISTIANE
"""

class Guichetier() :
    
    def __init__(self, solde, montant):
        self.solde =solde
        self.montant =montant
        
    def virement(self, solde):
        montant =  int(input("entrer le montant du virement "))
        if montant < int(solde) :
            self.solde -= montant
            print("votre nouveau solde est {}".format(self.solde))
            print("le virement a ete effectuer")
        else :
            print("solde insuffisant")

    def operation_internationnal(self, solde):
        montant = int(input("Donner le montant d'operation "))
        if montant < int(solde) :
            self.solde -= montant
            print("votre nouveau solde est {}".format(self.solde))
            print("l'operation internationnal a ete effectuer")                  
        else :
            print("solde insuffisant")
            
 # Programme Principale           
    
 
            
Client_Guichetier = {}
solde = 0
montant = 0
abo = Guichetier(solde, montant)
abo.virement(solde)
abo.operation_internationnal(solde)
