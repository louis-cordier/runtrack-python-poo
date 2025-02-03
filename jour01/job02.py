class Operation:
    def __init__(self, nombre1=12, nombre2=3):
        self.nombre1 = nombre1
        self.nombre2 = nombre2

# Instanciation de la classe
operation_instance = Operation()

# Affichage de l'objet instancié
print(operation_instance)

# Affichage des attributs
print(f"Le nombre1 est {operation_instance.nombre1}")
print(f"Le nombre2 est {operation_instance.nombre2}")
