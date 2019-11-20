#cette sous-classe est écrite par DOUMNINGA KLAMTE ARISTIDE
#Matricule 18B598FS
class controleur (PersonneBank):
    solde=int(input("solde"))
    montant=int(input("montant"))
    if solde<=0:
        print("pas de transaction")
    else:
        if solde<montant :
            print ("pas de transaction")
        else:
            print ("transaction=ok")
