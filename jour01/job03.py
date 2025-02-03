class Operation:
    def __init__(self, nombre1=12, nombre2=3):
        self.nombre1 = nombre1
        self.nombre2 = nombre2

    def addition(self):
        resultat = self.nombre1 + self.nombre2
        print(f"Le résultat de l'addition est {resultat}")

# Instanciation de la classe
operation_instance = Operation()

# Affichage de l'objet instancié
print(operation_instance)

# Affichage des attributs
print(f"Le nombre1 est {operation_instance.nombre1}")
print(f"Le nombre2 est {operation_instance.nombre2}")

# Appel de la méthode addition
operation_instance.addition()
