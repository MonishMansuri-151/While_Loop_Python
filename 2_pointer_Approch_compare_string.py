# duplicate find 2 pointer approch
s = "41623874"
last = len(s) - 1
start = 0
size = len(s) - 1
count = 0
total = 0
indicator = True
while start < size:
    if int(s[start]) + int(s[last]) == 11:
        print(s[start], s[last])
        total = int(s[start]) + int(s[last])
        print("sum of ", total)
        break

    last -= 1

    if start == last:
        # print("----------------------")
        start += 1
        last = len(s) - 1
    if indicator == True:
        count += 1
        indicator = True
# print(count)
