import numpy as np
import random

def get_random_matrix():
    return np.random.randint(1,101,size=(1,100))

def reshape(matrix,shape):
    try:
        res = matrix.reshape(shape)
    except ValueError as e:
        print(f"La forma no es correcta {e}")
        res = matrix
    return res

random_matrix = get_random_matrix()
user_shape = [
    int(input("Intodueix el numero de files: ")),
    int(input("Introdueix el numero de columnes: "))
]

print(random_matrix)
random_matrix = reshape(random_matrix,user_shape)
print(random_matrix)
print(f"Valor més gran {random_matrix.max()}")
print(f"Valor més petit: {random_matrix.min()}")