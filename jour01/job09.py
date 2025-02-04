class Produit:
    def __init__(self, nom, prixHT, TVA):
        self.nom = nom
        self.prixHT = prixHT
        self.TVA = TVA

    def CalculerPrixTTC(self):
        return self.prixHT * (1 + self.TVA / 100)

    def afficher(self):
        return f" Nom : {self.nom}, Prix HT : {self.prixHT}, TVA : {self.TVA}, Prix TTC : {self.CalculerPrixTTC()}"

    def modifierNom(self, nouveau_nom):
        self.nom = nouveau_nom

    def modifierPrix(self, nouveau_prix):
        self.prixHT = nouveau_prix

    def getNom(self):
        return self.nom

    def getPrixHT(self):
        return self.prixHT

    def getTVA(self):
        return self.TVA

# Création et modification des produits
produit1 = Produit("Laptop", 1000, 20)
produit2 = Produit("Smartphone", 800, 20)

produit1.modifierPrix(1200)
produit2.modifierNom("Phone Pro")

print(produit1.afficher())
print(produit2.afficher())