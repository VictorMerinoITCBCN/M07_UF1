import numpy as np

def primer_array():
    return np.array([88, 23, 39, 41])

def segon_array():
    return np.array([76.4, 21.7, 38.4, 41.2, 52.8, 68.9]).reshape(2,3)

def tercer_array():
    return np.array([12, 4, 9, 8]).reshape(4,1)

def mostrar_informacio(arr):
    #Mostra per pantalla informació del array
    print("--------------------------------------")
    print(f"Array: {arr}")
    print(f"Dimensió: {arr.ndim}")
    print(f"Tamany: {arr.shape}")
    print(f"Número total d'elements: {arr.size}")
    print(f"Tipus d'elements interns: {arr.dtype}")

array1 = primer_array()
array2 = segon_array()
array3 = tercer_array()

mostrar_informacio(array1)
mostrar_informacio(array2)
mostrar_informacio(array3)
