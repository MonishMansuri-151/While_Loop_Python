# 5.Write a Python program to check whether a given number is a Strong Number or not.
# A is a number where the .
# Example:
# 145 → 1! + 4! + 5! = 1 + 24 + 120 = 145
# 145
n = 175
n2 = n
i = 1
sum = 0
while n > 0:
    rem = n % 10
    n = n // 10
    fact = 1
    i = 1
    while i <= rem:
        fact = fact * i
        i = i + 1
    sum = sum + fact
print("sum of fact ", sum)
if sum == n2:
    print("Strong number ")
else:
    print("Week number")
