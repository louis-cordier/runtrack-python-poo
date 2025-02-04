class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def afficherLesPoints(self):
        print(f"Les coordonnées du point sont ({self.x}, {self.y})")

    def afficherX(self):
        print(f"La coordonnée X est {self.x}")

    def afficherY(self):
        print(f"La coordonnée Y est {self.y}")

    def changerX(self, new_x):
        self.x = new_x

    def changerY(self, new_y):
        self.y = new_y

# Instanciation d'un point
point1 = Point(5, 10)

# Affichage des coordonnées
point1.afficherLesPoints()
point1.afficherX()
point1.afficherY()

# Modification des coordonnées
point1.changerX(15)
point1.changerY(20)

# Affichage des nouvelles coordonnées
point1.afficherLesPoints()
