#cette sous-classe est écrite par DOUMNINGA KLAMTE ARISTIDE 18B598FS
Class controleur(personneBank):
    solde=int(input("solde"))
    montant=int(input("montant")
    if solde<=0:
       print("pas de transaction")
    else:
        if solde<montant:
            print("pas de transaction")
        else:
            print("transaction=ok')
