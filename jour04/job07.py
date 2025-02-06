import random

class Carte:
    def __init__(self, valeur, couleur):
        self.valeur = valeur
        self.couleur = couleur

    def __repr__(self):
        return f"{self.valeur} de {self.couleur}"


class Jeu:
    def __init__(self):
        valeurs = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Valet', 'Dame', 'Roi', 'As']
        couleurs = ['Pique', 'Cœur', 'Carreau', 'Trèfle']
        self.paquet = [Carte(valeur, couleur) for valeur in valeurs for couleur in couleurs]
        random.shuffle(self.paquet)

    def tirer_carte(self):
        return self.paquet.pop() if self.paquet else None

    def calculer_points(self, main):
        total = 0
        as_count = 0

        for carte in main:
            if carte.valeur in ['Valet', 'Dame', 'Roi']:
                total += 10
            elif carte.valeur == 'As':
                total += 11  # On suppose d'abord que l'As vaut 11
                as_count += 1
            else:
                total += int(carte.valeur)

        while total > 21 and as_count > 0:
            total -= 10  # On transforme un As de 11 en 1
            as_count -= 1

        return total

    def jouer(self):
        joueur = [self.tirer_carte(), self.tirer_carte()]
        croupier = [self.tirer_carte(), self.tirer_carte()]

        print(f"Vos cartes: {joueur}, Score: {self.calculer_points(joueur)}")
        print(f"Carte visible du croupier: {croupier[0]}")

        # Tour du joueur
        while self.calculer_points(joueur) < 21:
            action = input("Voulez-vous tirer une carte ? (o/n) : ").strip().lower()
            if action == 'o':
                joueur.append(self.tirer_carte())
                print(f"Vos cartes: {joueur}, Score: {self.calculer_points(joueur)}")
                if self.calculer_points(joueur) > 21:
                    print("Vous avez dépassé 21 ! Vous perdez.")
                    return
            else:
                break

        # Tour du croupier
        print(f"Cartes du croupier: {croupier}, Score: {self.calculer_points(croupier)}")
        while self.calculer_points(croupier) < 17:
            croupier.append(self.tirer_carte())
            print(f"Le croupier tire une carte: {croupier[-1]}")
            print(f"Cartes du croupier: {croupier}, Score: {self.calculer_points(croupier)}")

        # Résultat final
        joueur_score = self.calculer_points(joueur)
        croupier_score = self.calculer_points(croupier)

        if croupier_score > 21 or joueur_score > croupier_score:
            print("Félicitations, vous avez gagné !")
        elif joueur_score == croupier_score:
            print("Match nul !")
        else:
            print("Le croupier gagne !")


# Lancer une partie
jeu = Jeu()
jeu.jouer()
