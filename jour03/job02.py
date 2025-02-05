class CompteBancaire:
    def __init__(self, numero_compte, nom, prenom, solde, decouvert=False):
        self.__numero_compte = numero_compte
        self.__nom = nom
        self.__prenom = prenom
        self.__solde = solde
        self.__decouvert = decouvert
    
    def afficher(self):
        return f"Compte N°{self.__numero_compte} - Titulaire: {self.__nom} {self.__prenom} - Solde: {self.__solde} EUR - Découvert: {'Oui' if self.__decouvert else 'Non'}"
    
    def afficherSolde(self):
        return f"Solde actuel: {self.__solde} EUR"
    
    def versement(self, montant):
        self.__solde += montant
        return f"Versement de {montant} EUR effectué. Nouveau solde: {self.__solde} EUR"
    
    def retrait(self, montant):
        if self.__solde - montant < 0 and not self.__decouvert:
            return "Solde insuffisant pour effectuer ce retrait."
        self.__solde -= montant
        return f"Retrait de {montant} EUR effectué. Nouveau solde: {self.__solde} EUR"
    
    def agios(self, taux=5):
        if self.__solde < 0:
            self.__solde -= abs(self.__solde) * (taux / 100)
            return f"Agios appliqués. Nouveau solde: {self.__solde} EUR"
        return "Aucun agios appliqué. Solde positif."
    
    def virement(self, compte_destinataire, montant):
        if self.__solde - montant < 0 and not self.__decouvert:
            return "Virement refusé. Solde insuffisant."
        self.__solde -= montant
        compte_destinataire.versement(montant)
        return f"Virement de {montant} EUR effectué vers le compte N°{compte_destinataire.__numero_compte}" 

# Création des comptes
compte1 = CompteBancaire(101, "Dupont", "Jean", 1000)
compte2 = CompteBancaire(102, "Martin", "Paul", -200, decouvert=True)

# Vérification des informations des comptes
print(compte1.afficher())
print(compte2.afficher())

# Effectuer un virement de compte1 vers compte2 pour le remettre à zéro
print(compte1.virement(compte2, 200))

# Vérification après virement
print(compte1.afficher())
print(compte2.afficher())
