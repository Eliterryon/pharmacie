class Client:

    nom = ""
    credit = 0

    def __init__(self, nom, credit):
        self.nom = nom
        self.credit = credit

    def crediter(self, montant):
        self.credit -= montant

    def __str__(self):
        return ("Client(name={}, credit={})".format(self.nom, self.credit))