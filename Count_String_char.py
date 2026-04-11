# 📝 Problem: Given a string, count the total
# number of characters without using len().
str = "Hello"
i = 1
count = 0
while i <= len(str):
    count = count + 1
    i = i + 1
print("totalchr = ", count)
