n = 6
temp = n
i = 2
sum = 1
while n >= i:
    if n % i == 0:
        n = n // i
        # print(i
        sum = sum + i
    else:
        i = i + 1
if sum == temp:
    print("Perfect number ")
else:
    print("not perfect number ")
