# 📝 Problem: Given an integer N, check if it is a palindrome (reads same forward and backward)./
n = 121
temp = n
p = 0
while n > 0:
    rem = n % 10
    p = (p * 10) + rem
    n = n // 10
if temp == p:
    print("plindrome number")
else:
    print("not palindrome")
