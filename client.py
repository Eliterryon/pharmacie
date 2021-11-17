class Client:

    nom = ""
    credit = 0

    def __init__(self, nom, credit):
        self.nom = nom
        self.credit = credit

    def crediter(self, montant):
        self.credit -= montant

    def __str__(self):
        return ("Client(name={0}, credit={1})".format(self.nom, self.credit))

if __name__ == "__main__":
    m1 = Client("aspirine", 1.3)
    print(m1)