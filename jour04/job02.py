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

# Création d'un élève
eleve1 = Eleve()  # L'élève a 14 ans par défaut
eleve1.bonjour()  # Affiche "Hello"
eleve1.allerEnCours()  # Affiche "Je vais en cours"
eleve1.modifierAge(15)  # On change son âge à 15 ans
eleve1.afficherAge()  # Affiche "J’ai 15 ans"

# Création d'un professeur
professeur1 = Personne(40)  # Professeur avec 40 ans
professeur1.bonjour()  # Affiche "Hello"

# Instanciation d'un professeur avec une matière enseignée
prof1 = Professeur("Mathématiques")
prof1.enseigner()  # Affiche "Le cours va commencer"
