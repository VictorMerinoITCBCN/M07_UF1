def print_menu():
    print("0 - Sortir")
    print("1 - Introdueir contacte")

def add_contact():
    name = input("Nom: ")
    if name in contacts:
        print(f"{name} ya esta registrat")
        return
    
    age = int(input("Edad: "))

    contacts[name] = age

def menu():
    option = None
    while option != 0:
        print_menu()
        option = int(input("Opció: "))
        if option == 1: add_contact()
        
contacts = {}
menu()