user_num = int(input("Introdueix un nùmero de l' 1 al 10: "))

table = (user_num * i for i in range(1,11))

for i in table: print(i)