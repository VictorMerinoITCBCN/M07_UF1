user_num = int(input("Introdueix un nùmero del 10 al 100: "))

num_tuple = (i for i in range(1, user_num+1))

for i in num_tuple: print(i)