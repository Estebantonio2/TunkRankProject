import random

male_names = [
    "Liam", "Thiago", "Dylan", "Gael", "Mateo", 
    "Luis", "Juan", "Axel", "Ian", "Ángel", 
    "Santiago", "Lucas", "Carlos", "José", 
    "Iker", "Gabriel", "Mathias", "Sebastián", 
    "Diego", "Antonio"
    ]
female_names = [
    "Mia", "Alessia", "Camila", "Danna", "Zoe", 
    "Luciana", "Aitana", "María", "Briana", "Luz", 
    "Ariana", "Valentina", "Luana", "Sofia", "Emma", 
    "Antonella", "Emily", "Lia", "Kiara", "Ana"
    ]

def generate_adjacency_matrix(n, prob=0.5):
    matrix = [[0 for _ in range(n)] for _ in range(n)]
    
    for i in range(n):
        for j in range(n):
            if i != j:  # No se permite auto-direccionamiento (diagonal siempre 0)
                if random.random() < prob:
                    matrix[i][j] = 1
    
    return matrix

def print_matrix(matrix):
    """
    Imprime la matriz de adyacencia en formato legible.
    """
    print("matrix = [")
    for row in matrix:
        print(f"    {row},")
    print("]")

def generate_random_names(n):
    all_names = male_names + female_names
    selected_names = random.sample(all_names, min(n, len(all_names)))
    return selected_names

def print_names(names):
    """
    Imprime la lista de nombres en formato legible.
    """
    print(f"names = {names}")

def main():
    # Parámetro n para el tamaño de la matriz
    n = 5  # Puedes cambiar este valor

    # Generar la matriz de adyacencia
    adjacency_matrix = generate_adjacency_matrix(n, prob=0.5)

    # Imprimir la matriz
    print_matrix(adjacency_matrix)

    print()
    
    # Generar lista de nombres aleatorios
    random_names = generate_random_names(n)

    # Imprimir la lista de nombres
    print_names(random_names)

main()