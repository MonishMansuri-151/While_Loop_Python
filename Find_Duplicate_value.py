# find duplicat charcter
s = "rajaram"
current = 1
start = 0
count = 0
size = len(s) - 1
indicator = True
while current < size:
    print(s[start], s[current])
    if s[start] == s[current]:
        indicator = False
    current += 1
    if current == len(s):
        start += 1
        current = start + 1

    if indicator == False:
        # print(indicator)

        count += 1
    indicator = True
print(count)
