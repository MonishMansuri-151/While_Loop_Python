# 📝 Problem: Given a sentence (string), count the number of words (words are separated by single
# spaces).
s = "hello i love india hi"
i = 1
count = 1
while i <= len(s) - 1:
    if s[i] == " ":
        count = count + 1
    # print(i)
    i = i + 1
print(count)
