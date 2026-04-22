# 📝 Problem: Given N and a string of numbers separated by space
# (1 to N with one missing),
# find themissing number.
n = "1 2 4 5"
i = 0
num = ""
while i <= len(n) - 1:
    if n[i] != " ":
        num += n[i]
    else:
        i = i + 1
print(num)
