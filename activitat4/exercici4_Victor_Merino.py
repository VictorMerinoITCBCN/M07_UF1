import numpy as np
import random

def get_random_matrix_3x4():
    return np.random.randint(81, size=(3,4))
    
def reshape_to_4x3(matrix):
    last_column = matrix[:,-1]
    matrix_without_last_column = matrix[:,:-1]
    return np.append(matrix_without_last_column,last_column).reshape(4,3)

random_matrix_3x4 = get_random_matrix_3x4()
print(random_matrix_3x4)
random_matrix_4x3 = reshape_to_4x3(random_matrix_3x4)
print(random_matrix_4x3)