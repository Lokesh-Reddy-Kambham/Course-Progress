def square(num):
    return num * num
res = square(5)
print(res)

sq = lambda num:num*num
result = sq(6)
print(result)


div_modulus = lambda n1 , n2: (n1*n2, n1//n2)
output = div_modulus(10,2)
print(type(output))

