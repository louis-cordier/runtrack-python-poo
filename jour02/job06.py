from abc import ABC, abstractmethod

class Commande(ABC):
    def __init__(self, numero_commande):
        self.__numero_commande = numero_commande
        self.__plats = []  # Liste des plats [{"nom": nom, "prix": prix, "statut": statut}]
        self.__statut = "En cours"
    
    def ajouter_plat(self, nom_plat, prix):
        if self.__statut == "En cours":
            self.__plats.append({"nom": nom_plat, "prix": prix, "statut": self.__statut})
        else:
            raise Exception("Impossible d'ajouter un plat à une commande annulée ou terminée.")
    
    def annuler_commande(self):
        self.__statut = "Annulée"
    
    def terminer_commande(self):
        self.__statut = "Terminée"
    
    def __calculer_total(self):
        return sum(plat["prix"] for plat in self.__plats)
    
    def calculer_TVA(self, taux_TVA=20):
        return self.__calculer_total() * (taux_TVA / 100)
    
    def afficher_commande(self):
        return {
            "Numéro": self.__numero_commande,
            "Plats": self.__plats,
            "Statut": self.__statut,
            "Total HT": self.__calculer_total(),
            "TVA": self.calculer_TVA(),
            "Total TTC": self.__calculer_total() + self.calculer_TVA()
        }

# Création et gestion d'une commande
commande1 = Commande(101)
commande1.ajouter_plat("Pizza Margherita", 12)
commande1.ajouter_plat("Pâtes Carbonara", 15)
commande1.ajouter_plat("Tiramisu", 6)

# Affichage avant clôture avec une commande en cours
infos_avant = commande1.afficher_commande()

# Modification après clôture en ajoutant un nouveau plat (qui ne sera pas pris en compte)
commande1.terminer_commande()
try:
    commande1.ajouter_plat("Salade César", 8)
except Exception as e:
    erreur_ajout = str(e)

# Affichage après clôture avec la commande terminée
infos_apres = commande1.afficher_commande()

# Résultats affichés
print("Avant clôture:", infos_avant)
print("Erreur lors de l'ajout après clôture:", erreur_ajout)
print("Après clôture:", infos_apres)
