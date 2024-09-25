word_list = input("Introdueix de 1 a 3 paraules:").split(" ")

for word in word_list:
    print(word + ":")
    print(f" Numero de caracters: {len(word)}")
    print(f" Primer caracter: {word[0]} \n Ultim caracter: {word[-1]}")

