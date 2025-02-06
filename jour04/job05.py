import math  # Importation du module pour utiliser pi

class Forme:
    def aire(self):
        return 0


class Rectangle(Forme):
    def __init__(self, largeur, hauteur):
        self.largeur = largeur
        self.hauteur = hauteur

    def aire(self):  # Surcharge de la méthode aire()
        return self.largeur * self.hauteur


class Cercle(Forme):
    def __init__(self, radius):
        self.radius = radius

    def aire(self):  # Surcharge de la méthode aire()
        return math.pi * (self.radius ** 2)


# Instanciation d'un rectangle et d'un cercle
rectangle1 = Rectangle(10, 5)
cercle1 = Cercle(7)

# Affichage des résultats
print("Aire du rectangle :", rectangle1.aire())  # Devrait afficher 50
print("Aire du cercle :", cercle1.aire())  # Devrait afficher environ 153.94
