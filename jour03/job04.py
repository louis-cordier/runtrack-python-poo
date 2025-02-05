class Joueur:
    def __init__(self, nom, numero, position):
        self.nom = nom
        self.numero = numero
        self.position = position
        self.buts = 0
        self.passes_decisives = 0
        self.cartons_jaunes = 0
        self.cartons_rouges = 0

    def marquerUnBut(self):
        self.buts += 1
    
    def effectuerUnePasseDecisive(self):
        self.passes_decisives += 1
    
    def recevoirUnCartonJaune(self):
        self.cartons_jaunes += 1
    
    def recevoirUnCartonRouge(self):
        self.cartons_rouges += 1
    
    def afficherStatistiques(self):
        return {
            "Nom": self.nom,
            "Numéro": self.numero,
            "Position": self.position,
            "Buts": self.buts,
            "Passes décisives": self.passes_decisives,
            "Cartons jaunes": self.cartons_jaunes,
            "Cartons rouges": self.cartons_rouges
        }

class Equipe:
    def __init__(self, nom):
        self.nom = nom
        self.joueurs = []
    
    def ajouterJoueur(self, joueur):
        self.joueurs.append(joueur)
    
    def afficherStatistiquesJoueurs(self):
        return [joueur.afficherStatistiques() for joueur in self.joueurs]
    
    def mettreAJourStatistiquesJoueur(self, nom, action):
        for joueur in self.joueurs:
            if joueur.nom == nom:
                if action == "but":
                    joueur.marquerUnBut()
                elif action == "passe":
                    joueur.effectuerUnePasseDecisive()
                elif action == "jaune":
                    joueur.recevoirUnCartonJaune()
                elif action == "rouge":
                    joueur.recevoirUnCartonRouge()
                return joueur.afficherStatistiques()
        return None

# Création des équipes
team1 = Equipe("FC Barcelone")
team2 = Equipe("Olympique de Marseille")

# Ajout des joueurs
j1 = Joueur("Robert Lewandowski", 10, "Attaquant")
j2 = Joueur("Valentin Carboni", 7, "Milieu")
j3 = Joueur("Amine Harit", 11, "Ailier")

team1.ajouterJoueur(j1)
team2.ajouterJoueur(j2)
team2.ajouterJoueur(j3)

# Simulation d'un match
team1.mettreAJourStatistiquesJoueur("Robert Lewandowski", "but")
team2.mettreAJourStatistiquesJoueur("Valentin Carboni", "passe")
team2.mettreAJourStatistiquesJoueur("Amine Harit", "jaune")

# Affichage des statistiques après match
stats_team1 = team1.afficherStatistiquesJoueurs()
stats_team2 = team2.afficherStatistiquesJoueurs()

print("Statistiques de FC Barcelone:", stats_team1)
print("Statistiques de Olympique de Marseille:", stats_team2)
