import numpy as np

#Genera un array end*end amb un rang de numeros (indicats per l'usuari) ascendents a la diagonal de l'array
def get_diagonal_array(start=0,end=10):
    return np.diag(range(start, end+1))

#Crida a la funció i guarda el resultat
nd_array = get_diagonal_array(end=49)
np.save("./exercici1.npy", nd_array)

#Mostra per pantalla informació del array
print(f"Array: {nd_array}")
print(f"Dimensió: {nd_array.ndim}")
print(f"Tamany: {nd_array.shape}")
print(f"Número total d'elements: {nd_array.size}")
print(f"Tipus d'elements interns: {nd_array.dtype}")