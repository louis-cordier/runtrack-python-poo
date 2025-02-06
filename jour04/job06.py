class Vehicule:
    def __init__(self, marque, modele, annee, prix):
        self.marque = marque
        self.modele = modele
        self.annee = annee
        self.prix = prix

    def informationsVehicule(self):
        print(f"Marque = {self.marque}")
        print(f"Model = {self.modele}")
        print(f"Année = {self.annee}")
        print(f"Prix = {self.prix}")


class Voiture(Vehicule):
    def __init__(self, marque, modele, annee, prix):
        super().__init__(marque, modele, annee, prix)
        self.portes = 4  # Attribut spécifique à Voiture

    def informationsVehicule(self):  # Surcharge de la méthode
        super().informationsVehicule()
        print(f"Nombre de porte = {self.portes}")


# Instanciation d'une voiture
voiture1 = Voiture("Mercedes", "Class A", 2020, 18500)

# Affichage des informations de la voiture
voiture1.informationsVehicule()

# ------------------suite job06 ------------------------------

class Moto(Vehicule):
    def __init__(self, marque, modele, annee, prix):
        super().__init__(marque, modele, annee, prix)
        self.roue = 2  # Attribut spécifique à Moto

    def informationsVehicule(self):  # Surcharge de la méthode
        super().informationsVehicule()
        print(f"Nombre de roue = {self.roue}")


# Instanciation d'une moto
moto1 = Moto("Yamaha", "1200 Vmax", 1987, 4500)

# Affichage des informations de la moto
moto1.informationsVehicule()
