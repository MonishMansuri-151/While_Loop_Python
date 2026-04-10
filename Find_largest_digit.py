# find the largest digit of  a number
n = 6498
temp = 0
while n != 0:
    rem = n % 10
    n = n // 10
    if rem >= temp:
        temp = rem
print("last digit ", temp)
