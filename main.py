from medicament import Medicament
from client import Client



ListeClient = []
ListeMedicament = []



def affichage():
    print("Affichage des stocks")
    for medoc in ListeMedicament :
        print(medoc)
    print("Affichage des credits")
    for client in ListeClient :
        print(client)

def approvisionnement():
    medoc = None
    print("Nom du Medicament?:")
    while medoc == None :
        medoc = lireTable(ListeMedicament)
        if medoc == None :
            print("Medicament inconnu. Veuilliez recommencer")

    print("Donner la Quantite :")
    quantite = inputInt()
    medoc.approvisionnement(quantite)

def achat():
    medoc = None
    client = None
    print("Nom du Medicament?:")
    while medoc == None :
        medoc = lireTable(ListeMedicament)
        if medoc == None :
            print("Medicament inconnu. Veuilliez recommencer")

    print("Nom du client?:")
    while client == None :
        client = lireTable(ListeClient)
        if client == None :
            print("Client inconnu. Veuilliez recommencer")

    print("quel est le montant du paiement?")
    quantitePaiyment = inputFloat()
    print("quelle est la quantite achetee?")
    quantiteMedoc = inputInt()

    while(quantiteMedoc>=medoc.stock):
        print("le stock pour ce medicament est de :"+ medoc.stock +" veuilleur choisire un nombre valable")
        quantiteMedoc = inputInt()

    medoc.debit(lireTable)

    client.crediter(quantitePaiyment-(quantiteMedoc*medoc.prix))


def quitter():
    print ("Programme termine!")

 ##################### lecture des tables ########################

def lireTable(Liste):
    nom = input()
    for obj in Liste :
        if (obj.nom == nom):
            return obj
    return None

 ##################### definition des inpute #####################

def inputFloat():
    while True :
        floatInpute = input()
        try:
            valeur = float(floatInpute)
            return valeur
        except:
            print("Veuillez entrer un monbre")

def inputInt():
    while True :
        intInpute = input()
        try:
            valeur = int(intInpute)
            return valeur
        except:
            print("Veuillez entrer un monbre entier")

##################### main loop ##################################

ListeClient.append(Client("Malfichu",0.0))
ListeClient.append(Client("Palichon",0.0))
ListeMedicament.append(Medicament("Aspiron", 20.40, 5))
ListeMedicament.append(Medicament("Rhinoplexil", 19.15, 5))

numberIn = ""
while numberIn != "4":
    print("")
    print("")
    print("1 : Achat de medicament")
    print("2 : Approvisionnement en  medicaments")
    print("3 : Etats des stocks et des credits")
    print("4 : Quitter")
    numberIn = input()
    if (numberIn == "1" ):
        achat()
    elif (numberIn == "2" ):
        approvisionnement()
    elif (numberIn == "3" ):
        affichage()
    elif (numberIn == "4" ):
        quitter()
        break
