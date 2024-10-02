alphabet = [chr(num) for num in range(97,123)]


alphabet_with_no_3 = tuple((alphabet[i] for i in range(len(alphabet)) if i%3 == 0))

print(alphabet)
print(alphabet_with_no_3)