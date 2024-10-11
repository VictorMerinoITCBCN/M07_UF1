user_phrase = input("Introdueix una frase: ")
user_tuple = tuple(user_phrase.replace(" ", ""))

print(user_tuple)

user_phrase_no_repetitions = set(user_tuple)

print(user_phrase_no_repetitions)