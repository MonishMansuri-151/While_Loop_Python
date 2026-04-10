# count the n number of digits 12345 => 5 digits
n = 455432
count = 0
while n != 0:
    rem = n % 10
    count = count + 1
    n = n // 10
print(count)
