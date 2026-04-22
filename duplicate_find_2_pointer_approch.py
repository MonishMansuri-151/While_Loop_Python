# duplicate find 2 pointer approch
s = "rajaram"
last = len(s) - 1
start = 0
size = len(s) - 1
count = 0
indicator = True
while start < size:
    print(s[start], s[last])
    if s[start] == s[last]:
        indicator = False

    last -= 1

    if start == last:
        print("----------------------")
        start += 1
        last = len(s) - 1
    if indicator == True:
        count += 1
        indicator = True
print(count)
