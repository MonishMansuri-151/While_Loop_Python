data = "madamimadam"
first = 0
last = len(data) - 1
a = True

while first < last:
    # print("first =", first, "data =>", data[first], "last=", last, "data =>", data[last])
    if data[first] != data[last]:
        a = False
        break
    first += 1
    last -= 1

if a == False:
    print("not palindrome")
else:
    print("palindrome")


# data = "naman"
# x = 0
# y = len(data) - 1
# a = True
# while x <= len(data) - 1:
#     print("x =", x, "data =>", data[x], "y =", y, "data => ", data[y])
#     if data[x] != data[y]:
#         a = False
#     x = x + 1
#     y = y - 1
# if a == False:
#     print("not palindrome")
# else:
#     print("palindrome ")
