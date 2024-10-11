user_nums = input("Introdueix 10 numeros separats per espais: ")
user_nums_list = [int(i) for i in user_nums.split(" ")]
user_nums_list.sort()

user_nums_tuple = tuple(user_nums_list)

for i in user_nums_list: print(i)