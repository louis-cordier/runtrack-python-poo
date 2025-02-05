import random

class Personnage:
    def __init__(self, nom, vie):
        self.nom = nom
        self.vie = vie
    
    def attaquer(self, adversaire):
        degats = random.randint(5, 15)
        adversaire.vie -= degats
        print(f"{self.nom} attaque {adversaire.nom} et lui inflige {degats} points de dégâts.")
        
    def est_vivant(self):
        return self.vie > 0

class Jeu:
    def __init__(self):
        self.niveau = None

    def choisirNiveau(self):
        while True:
            try:
                niveau = int(input("Choisissez un niveau (1: Facile, 2: Moyen, 3: Difficile) : "))
                if niveau in [1, 2, 3]:
                    self.niveau = niveau
                    break
                else:
                    print("Veuillez choisir un niveau valide (1, 2 ou 3).")
            except ValueError:
                print("Entrée invalide. Veuillez entrer un nombre.")
    
    def lancerJeu(self):
        if self.niveau == 1:
            vie_joueur, vie_ennemi = 50, 30
        elif self.niveau == 2:
            vie_joueur, vie_ennemi = 40, 40
        else:
            vie_joueur, vie_ennemi = 30, 50
        
        joueur = Personnage("Joueur", vie_joueur)
        ennemi = Personnage("Ennemi", vie_ennemi)
        
        while joueur.est_vivant() and ennemi.est_vivant():
            joueur.attaquer(ennemi)
            if ennemi.est_vivant():
                ennemi.attaquer(joueur)
            print(f"{joueur.nom}: {joueur.vie} PV | {ennemi.nom}: {ennemi.vie} PV\n")
        
        if joueur.est_vivant():
            print("Vous avez gagné !")
        else:
            print("Vous avez perdu...")

# Exécution du jeu
jeu = Jeu()
jeu.choisirNiveau()
jeu.lancerJeu()
