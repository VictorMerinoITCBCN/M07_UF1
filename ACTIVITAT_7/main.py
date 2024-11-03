from read import read_users
from create_table import create_user_table
from create import create_user
from update import update_user
from delete import delete_user

import uuid

def display_options():
    print("0) SORTIR")
    print("1) MOSTRAR USUARIS")
    print("2) CREAR TAULA")
    print("3) CREAR USUARI")
    print("4) ACTUALITZAR USUARI")
    print("5) ELIMINAR USUARI")

def display_users():
    response = read_users()

    if response["status"] == -1: 
        print(response["msg"])
        return

    users = response["users"]

    print(response["msg"])
    for user in users:
        print(user)

def create():
    id = uuid.uuid4()

    name = input("Introdueix el nom: ")
    last_name = input("Introdueix el cognom: ")
    age = int(input("Introdueix l'edat: "))
    email = input("Introdueix el correu: ")
    phone = int(input("Introdueix el nùmero de tel.: "))

    response = create_user(id, name, last_name, age, email, phone)
    print(response["msg"])

def update():
    id = input("Introdueix la id del usuari a actualitzar: ")

    name = input("Introdueix el nou nom (opcional): ")
    last_name = input("Introdueix el nou cognom (opcional): ")
    age = input("Introdueix la nova edad (opcional): ")
    email = input("Introdueix el nou email (opcional): ")
    phone = input("Introdueix el nou tel. (opcional): ")

    response = update_user(id, name, last_name, age, email, phone)
    print(response["msg"])

def delete():
    id = input("Introdueix la id del usuari a eliminar: ")

    response = delete_user(id)
    print(response["msg"])
    

def menu():
    option = None
    while option != 0:
        display_options()
        option = int(input("Selecciona una opció: "))

        if option == 1: display_users()
        elif option == 2: create_user_table()
        elif option == 3: create()
        elif option == 4: update()
        elif option == 5: delete()

menu()