# 📝 Problem: Given base B and exponent E, compute B^E using only while loop and multiplication.
value = 8
pow = 2
result = 1
while pow > 0:
    result = result * value
    pow = pow - 1
print(result)
