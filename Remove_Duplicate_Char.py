# 📝 Problem: Given a string, remove duplicate characters and keep only the first occurrence.
word = "Hello"
i = 0
result = ""
while i <= len(word) - 1:
    if word[i] not in result:
        result += word[i]

    i = i + 1
print(result)
