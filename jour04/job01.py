class Personne:
    def __init__(self, age=14):  # Age par défaut : 14
        self.age = age

    def afficherAge(self):
        print(f"Âge de la personne : {self.age}")

    def bonjour(self):
        print("Hello")

    def modifierAge(self, nouvel_age):
        self.age = nouvel_age


class Eleve(Personne):  # Hérite de Personne
    def allerEnCours(self):
        print("Je vais en cours")

    def afficherAge(self):
        print(f"J’ai {self.age} ans")


class Professeur:
    def __init__(self, matiereEnseignee):
        self.__matiereEnseignee = matiereEnseignee  # Attribut privé

    def enseigner(self):
        print("Le cours va commencer")


# Instanciation d'une Personne et d'un Eleve
personne1 = Personne()
eleve1 = Eleve()

# Affichage de l'âge par défaut de l'élève
eleve1.afficherAge()  # Devrait afficher "J’ai 14 ans"
