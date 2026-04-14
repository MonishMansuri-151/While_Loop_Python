# Problem: Given two integers A and B, find their Greatest Common Divisor (GCD).
a = 48
b = 18
i = 2
gcd = 1
while i <= b:
    if a % i == 0 and b % i == 0:
        a = a // i
        b = b // i
        gcd = gcd * i
    else:
        i = i + 1
print("GCD =>", gcd)
