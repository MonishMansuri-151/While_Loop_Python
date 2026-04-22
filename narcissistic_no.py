# narcissistic number (also known as an Armstrong number or perfect digital invariant)
#  is a number that is the sum of its own digits each raised to the power of the total number of digits.
#  For example, 153 is a 3-digit number where
n = 153
n3 = n
n2 = n
total = 0
count = 0
while n2 != 0:
    rem = n2 % 10
    n2 = n2 // 10
    count = count + 1
# print(count)
while n > 0:
    rem = n % 10
    n = n // 10
    total = total + (rem**count)
print(total)
if n3 == total:
    print("narcissistic number")
else:
    print("not narcissistic number ")


# easy way use built in function (len () )
# n = 3456
# original = n

# count = len(str(n))  # easy way

# total = 0
# while n > 0:
#     digit = n % 10
#     total += digit ** count
#     n //= 10

# if original == total:
#     print("narcissistic number")
# else:
#     print("not narcissistic number")
