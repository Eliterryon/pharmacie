class Medicament:

    nom = ""
    prix = 0
    stock = 0

    def __init__(self, nom, prix, stock):
        self.nom = nom
        self.prix = prix
        self.stock = stock

    def approvisionnement(self, montant):
        self.stock += montant

    def debit(self, montant):
        self.stock -= montant

    def __str__(self):
        return ("Medicament(name={}, prix={}, stock={})".format(self.nom, self.prix,self.stock))


if __name__ == "__main__":
    m1 = Medicament("aspirine", 1.3,25)
    print(str(m1))