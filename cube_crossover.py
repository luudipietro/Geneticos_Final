import random

def cube_crossover(parent1, parent2):
    """
    Realiza el cruzamiento de cubo (hypercube crossover) para dos padres.
    Ambos padres deben ser listas o arreglos numéricos de la misma longitud.
    """
    child1 = []
    child2 = []
    
    for p1, p2 in zip(parent1, parent2):
        # Generar un random para cada uno
        rand = random.random()
        
        c1 = p1 + rand * (p2 - p1)
        c2 = p2 + rand * (p1 - p2)
        
        child1.append(c1)
        child2.append(c2)
        
    return child1, child2

# --- Ejemplo de uso ---
# Supongamos un problema de optimización con 3 variables (genes)
padre_A = [1.0, 5.0, 10.0]
padre_B = [4.0, 1.0, 20.0]

hijo_1, hijo_2 = cube_crossover(padre_A, padre_B)

print(f"Hijo 1: {hijo_1}")
print(f"Hijo 2: {hijo_2}")