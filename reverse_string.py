# 📝 Problem: Given a string, reverse it using a while loop.
str = "hello"
i = len(str) - 1
print(i)
empt = ""
while i >= 0:
    empt += str[i]
    i = i - 1
print(empt)
