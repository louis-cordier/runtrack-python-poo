class Livre:
    def __init__(self, titre, auteur, nb_pages):
        self.__titre = titre
        self.__auteur = auteur
        self.__nb_pages = nb_pages if nb_pages > 0 else 0  # Initialisation avec validation
        self.__disponible = True  # Par défaut, le livre est disponible
        self.__emprunte = False  # Variable pour savoir si le livre est emprunté ou non

    # Accesseurs (getters)
    def get_titre(self):
        return self.__titre
    
    def get_auteur(self):
        return self.__auteur
    
    def get_nb_pages(self):
        return self.__nb_pages

    def get_disponible(self):
        return self.__disponible

    # Mutateurs (setters)
    def set_titre(self, titre):
        self.__titre = titre
    
    def set_auteur(self, auteur):
        self.__auteur = auteur
    
    def set_nb_pages(self, nb_pages):
        if nb_pages > 0:
            self.__nb_pages = nb_pages
        else:
            print("Erreur : Le nombre de pages doit être un nombre entier positif.")

    # Vérification de la disponibilité du livre
    def verification(self):
        return self.__disponible
    
    # Emprunter le livre
    def emprunter(self):
        if not self.__emprunte:  # Vérifie si le livre a déjà été emprunté
            self.__emprunte = True
            self.__disponible = False
            print(f"Le livre '{self.__titre}' a été emprunté.")
        else:
            print(f"Le livre '{self.__titre}' est déjà emprunté.")
    
    # Rendre le livre
    def rendre(self):
        if self.__emprunte:  # Vérifie si le livre a bien été emprunté
            self.__emprunte = False
            self.__disponible = True
            print(f"Le livre '{self.__titre}' a été rendu.")
        else:
            print(f"Le livre '{self.__titre}' n'a pas été emprunté, il est déjà disponible.")

# Exemple d'utilisation
livre = Livre("1984", "George Orwell", 328)

# Vérification de la disponibilité avant l'emprunt
if livre.verification():
    livre.emprunter()  # Le livre est emprunté

# Essayer de réemprunter le même livre
livre.emprunter()  # Affichera que le livre est déjà emprunté

# Rendre le livre
livre.rendre()

# Essayer de rendre un livre qui n'a pas été emprunté
livre.rendre()  # Affichera que le livre n'a pas été emprunté
