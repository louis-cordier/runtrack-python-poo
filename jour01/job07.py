class Personnage:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def gauche(self):
        self.x -= 1

    def droite(self):
        self.x += 1

    def haut(self):
        self.y -= 1

    def bas(self):
        self.y += 1

    def position(self):
        return (self.x, self.y)

# Instanciation d'un personnage
personnage = Personnage(0, 0)

# Déplacement du personnage
personnage.droite()
personnage.bas()

# Affichage de la position
print(f"Position du personnage: {personnage.position()}")
