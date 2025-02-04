class Animal:
    def __init__(self):
        self.age = 0
        self.prenom = ""

    def vieillir(self):
        self.age += 1

    def nommer(self, nom):
        self.prenom = nom

# Instanciation d'un animal
animal = Animal()

# Affichage de l'âge initial
print(f"L'âge de l'animal {animal.age} ans")

# Faire vieillir l'animal
animal.vieillir()
print(f"L'âge de l'animal {animal.age} ans")

# Nommer l'animal
animal.nommer("Luna")
print(f"L'animal se nomme {animal.prenom}")