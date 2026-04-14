# 📝 Problem: Print the first N terms of the Fibonacci series using a while loop.
n = int(input("Enter a number : "))
i = 0
a = 0
b = 1
temp = 0
while i <= n:
    print(a)
    temp = a + b  # a+b = 1
    a = b  # a = 1
    b = temp  # b = temp b => 1

    i = i + 1
