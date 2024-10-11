def recursive_sum(num, sum):
    if num == 0: return sum

    sum+= num
    return recursive_sum(num-1,sum)

print(recursive_sum(5,0))