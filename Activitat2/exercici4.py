def print_menu():
    print("0 - Sortir")
    print("1 - Sumar")
    print("2 - Restar")
    print("3 - Multiplicar")
    print("4 - Dividir")

def sum(num1, num2): return num1 + num2

def substract(num1, num2) : return num1 - num2

def multiply(num1, num2) : return num1 * num2

def div(num1, num2): return num1 / num2

def menu(option, num1, num2):
    if option == 0: return ""
    if option == 1: return sum(num1, num2)
    if option == 2: return substract(num1, num2)
    if option == 3: return multiply(num1, num2)
    if option == 4: return div(num1, num2) 
    
    print("Introdoeix una opció correcte: ")
    return select_option()

def select_option(num1, num2):
    print_menu()
    option = int(input("Selecciona una opció: "))
    return "Resultat: " + str(menu(option, num1, num2))

num1 = int(input("Introdueix un numero: "))
num2 = int(input("Introdueix un altre numero: "))

print(select_option(num1, num2))