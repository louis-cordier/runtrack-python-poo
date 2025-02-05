class Tache:
    def __init__(self, titre, description, statut="À faire"):
        self.titre = titre
        self.description = description
        self.statut = statut
    
    def marquerCommeFinie(self):
        self.statut = "Terminée"
    
    def __repr__(self):
        return f"{self.titre} - {self.description} [{self.statut}]"


class ListeDeTaches:
    def __init__(self):
        self.taches = []
    
    def ajouterTache(self, tache):
        self.taches.append(tache)
    
    def supprimerTache(self, titre):
        self.taches = [t for t in self.taches if t.titre != titre]
    
    def marquerCommeFinie(self, titre):
        for t in self.taches:
            if t.titre == titre:
                t.marquerCommeFinie()
                break
    
    def afficherListe(self):
        return self.taches
    
    def filterListe(self, statut):
        return [t for t in self.taches if t.statut == statut]


# Création des tâches
tache1 = Tache("Faire les courses", "Acheter du lait et du pain")
tache2 = Tache("Réviser Python", "Faire les exercices sur les classes")
tache3 = Tache("Sport", "Courir 30 minutes")

# Gestion de la liste des tâches
liste_taches = ListeDeTaches()
liste_taches.ajouterTache(tache1)
liste_taches.ajouterTache(tache2)
liste_taches.ajouterTache(tache3)

# Suppression d'une tâche
liste_taches.supprimerTache("Sport")

# Marquer une tâche comme finie
liste_taches.marquerCommeFinie("Réviser Python")

# Affichage des tâches
print("Toutes les tâches:", liste_taches.afficherListe())
print("Tâches à faire:", liste_taches.filterListe("À faire"))
