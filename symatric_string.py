s = "khokho"
mid = len(s) // 2
last = len(s)
i = 0
result = ""
word = ""
while i < mid:

    while mid < last:
        result += s[mid]
        break
    word += s[i]
    break
print(result)
print(word)
if result == word:
    print("Symatric String..... ")
else:
    print("Not Symatric String ..!")
