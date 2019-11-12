#cette sous-classe est écrite par DOUMNINGA KLAMTE ARISTIDE 18B598FS
Class controleur (PersonneBank):
    solde=int(intput("solde"))
    montant=int(intput ("montant"))
    if solde<=0:
       print("pas de transaction")
     else:
         if solde<montant:
            print("pas de transaction")
         else:
            print("transaction=ok")
