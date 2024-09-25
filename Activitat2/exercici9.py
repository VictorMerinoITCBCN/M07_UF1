word1 = input("Paraula 1:")
word2 = input("Paraula 2:")

word1 , word2 = word2[0] + word1[1:] , word1[0] + word2[1:]

print(f"Paraula 1: {word1}")
print(f"Paraula 2: {word2}")