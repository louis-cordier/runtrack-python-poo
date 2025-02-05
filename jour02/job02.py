class Livre:
    def __init__(self, titre, auteur, nb_pages):
        self.__titre = titre
        self.__auteur = auteur
        self.__nb_pages = nb_pages if nb_pages > 0 else 0  # Initialisation, vérifie que nb_pages est positif

    # Accesseurs (getters)
    def get_titre(self):
        return self.__titre
    
    def get_auteur(self):
        return self.__auteur
    
    def get_nb_pages(self):
        return self.__nb_pages

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

# Exemple d'utilisation
livre = Livre("1984", "George Orwell", 328)
print(f"Titre : {livre.get_titre()}")
print(f"Auteur : {livre.get_auteur()}")
print(f"Nombre de pages : {livre.get_nb_pages()}")

# Essayer de changer le nombre de pages avec une valeur invalide
livre.set_nb_pages(-50)  # Affichera un message d'erreur
print(f"Nombre de pages après tentative de modification : {livre.get_nb_pages()}")
