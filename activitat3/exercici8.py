user_nums = input("Introdueix 10 numeros: ")
nums = [int(num) for num in user_nums.split(" ")]

sum_nums = sum(nums)
average_nums = sum_nums/len(nums)

nums.append(sum_nums)
nums.append(average_nums)

print(f"numeros: {nums}")
print(f"suma dels numeros: {sum_nums}")
print(f"mitjana: {average_nums}")