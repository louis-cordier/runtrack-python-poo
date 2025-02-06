class Rectangle:
    def __init__(self, longueur, largeur):
        self.__longueur = longueur
        self.__largeur = largeur

    # Getters (Assesseurs)
    def get_longueur(self):
        return self.__longueur

    def get_largeur(self):
        return self.__largeur

    # Setters (Mutateurs)
    def set_longueur(self, longueur):
        self.__longueur = longueur

    def set_largeur(self, largeur):
        self.__largeur = largeur

    # Méthodes de calcul
    def perimetre(self):
        return 2 * (self.__longueur + self.__largeur)

    def surface(self):
        return self.__longueur * self.__largeur


class Parallelepipede(Rectangle):
    def __init__(self, longueur, largeur, hauteur):
        super().__init__(longueur, largeur)
        self.hauteur = hauteur  # Nouvel attribut

    def volume(self):
        return self.surface() * self.hauteur


# Instanciation d'un Rectangle
rectangle1 = Rectangle(10, 5)

# Vérification des méthodes
print("Périmètre du rectangle:", rectangle1.perimetre())  # Devrait afficher 30
print("Surface du rectangle:", rectangle1.surface())  # Devrait afficher 50

# Instanciation d'un Parallélépipède
parallelepipede1 = Parallelepipede(10, 5, 4)

# Vérification des méthodes
print("Volume du parallélépipède:", parallelepipede1.volume())  # Devrait afficher 200
