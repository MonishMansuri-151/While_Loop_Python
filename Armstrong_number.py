n = 370
temp = n
total = 0
while n != 0:
    rem = n % 10
    n = n // 10
    total = total + rem**3
if temp == total:
    print("Armstrong number ")
else:
    print("Not Armstrong !")
