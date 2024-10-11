MONTHS = ("Gener","Febrer","Març","abril","maig","Juny","Juliol","Agost","Setembre","Octubre","Novembre","Desembre")

user_option = int(input("Introdueix un nùmero del 0 al 12(0 per sortir): "))

if user_option <= 0 or user_option > 12: exit()

print(MONTHS[user_option-1])