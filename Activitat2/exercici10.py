import random

random_num = random.randrange(1,100)

attemps = 0
user_num = None

while user_num != random_num:
    user_num = input("Introdueïx un número del 1 al 100: ")
    if type(user_num) != int: continue

    if user_num == random_num: print(f"Has trobat el número secret {user_num}")
    elif user_num < random_num: print(f"El número és més gran que {user_num}")
    elif user_num > random_num: print(f"El número és més petit que {user_num}")