class Student:
    def __init__(self, nom, prenom, numero_etudiant):
        self.__nom = nom
        self.__prenom = prenom
        self.__numero_etudiant = numero_etudiant
        self.__credits = 0  # Nombre de crédits initialisé à 0

    # Accesseur pour récupérer le nombre de crédits
    def get_credits(self):
        return self.__credits

    # Mutateur pour ajouter des crédits
    def add_credits(self, nombre):
        if nombre > 0:
            self.__credits += nombre
        else:
            print("Erreur : le nombre de crédits ajouté doit être supérieur à zéro.")

    # Méthode pour afficher les informations de l'étudiant
    def afficher_credits(self):
        print(f"Le nombre de crédits de {self.__prenom} {self.__nom} est de {self.__credits} points.")

# Instanciation de l'étudiant John Doe avec le numéro 145
etudiant = Student("Doe", "John", 145)

# Ajout de crédits à trois reprises
etudiant.add_credits(10)
etudiant.add_credits(10)
etudiant.add_credits(10)

# Affichage du total de crédits
etudiant.afficher_credits()

# -------------------------------- Deuxieme partie du job ----------------------------------------------

class Student:
    def __init__(self, nom, prenom, numero_etudiant):
        self.__nom = nom
        self.__prenom = prenom
        self.__numero_etudiant = numero_etudiant
        self.__credits = 0  # Nombre de crédits initialisé à 0
        self.__level = self.__student_eval()  # Définition du niveau basé sur les crédits

    # Accesseur pour récupérer le nombre de crédits
    def get_credits(self):
        return self.__credits

    # Mutateur pour ajouter des crédits
    def add_credits(self, nombre):
        if nombre > 0:
            self.__credits += nombre
            self.__level = self.__student_eval()  # Mettre à jour le niveau après ajout
        else:
            print("Erreur : le nombre de crédits ajouté doit être supérieur à zéro.")

    # Méthode privée pour évaluer le niveau de l'étudiant
    def __student_eval(self):
        if self.__credits >= 90:
            return "Excellent"
        elif self.__credits >= 80:
            return "Très bien"
        elif self.__credits >= 70:
            return "Bien"
        elif self.__credits >= 60:
            return "Passable"
        else:
            return "Insuffisant"

    # Méthode pour afficher les informations de l'étudiant
    def student_info(self):
        print(f"Nom = {self.__nom}")
        print(f"Prénom = {self.__prenom}")
        print(f"id = {self.__numero_etudiant}")
        print(f"Niveau = {self.__level}")

# Instanciation de l'étudiant John Doe avec le numéro 145
etudiant = Student("Doe", "John", 145)

# Ajout de crédits à trois reprises
etudiant.add_credits(10)
etudiant.add_credits(25)
etudiant.add_credits(35)  # Total : 10+25+35 = 70 crédits

# Affichage des informations de l'étudiant
etudiant.student_info()
