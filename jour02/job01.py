class Rectangle:
    def __init__(self, longueur, largeur):
        self.__longueur = longueur  # Attribut privé pour la longueur
        self.__largeur = largeur    # Attribut privé pour la largeur
    
    # Accesseur pour la longueur
    def get_longueur(self):
        return self.__longueur
    
    # Mutateur pour la longueur
    def set_longueur(self, longueur):
        self.__longueur = longueur
    
    # Accesseur pour la largeur
    def get_largeur(self):
        return self.__largeur
    
    # Mutateur pour la largeur
    def set_largeur(self, largeur):
        self.__largeur = largeur
    
    # Méthode pour afficher les dimensions du rectangle
    def afficher_dimensions(self):
        print(f"Longueur: {self.__longueur}, Largeur: {self.__largeur}")


# Création d'un rectangle avec longueur 10 et largeur 5
rectangle = Rectangle(10, 5)

# Affichage des dimensions initiales
rectangle.afficher_dimensions()

# Modification de la longueur et de la largeur
rectangle.set_longueur(15)
rectangle.set_largeur(8)

# Affichage des nouvelles dimensions après modification
rectangle.afficher_dimensions()
