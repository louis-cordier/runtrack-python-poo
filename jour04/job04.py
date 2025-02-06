class Forme:
    def aire(self):
        return 0


class Rectangle(Forme):
    def __init__(self, largeur, hauteur):
        self.largeur = largeur
        self.hauteur = hauteur

    def aire(self):  # Surcharge de la méthode aire()
        return self.largeur * self.hauteur


# Instanciation d'un rectangle
rectangle1 = Rectangle(10, 5)

# Affichage du résultat de la méthode aire()
print("Aire du rectangle :", rectangle1.aire())  # Devrait afficher 50
