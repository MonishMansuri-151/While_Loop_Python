n = 6
i = 2

while i <= n:
    if n % i == 0:
        n = n // i
        print(i)

    else:
        i = i + 1
