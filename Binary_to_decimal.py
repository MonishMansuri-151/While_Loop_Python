# 📝 Problem: Given a binary number as a string, convert it to decimal using a while loop.
binary = 1010
res = 1
sum = 0
i = 0
# decimal=∑(digit×2position)
while 0 < binary:
    rem = binary % 10
    binary = binary // 10
    res = rem * (2**i)
    sum = sum + res
    i = i + 1
print(sum)
