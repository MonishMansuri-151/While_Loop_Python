data = "naman"
x = 0
y = len(data) - 1
a = True

while x < y:
    print("x =", x, "data =>", data[x], "y =", y, "data =>", data[y])
    if data[x] != data[y]:
        a = False
        break
    x += 1
    y -= 1

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
