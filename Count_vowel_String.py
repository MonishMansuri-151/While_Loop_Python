s = "hellomonish"
count = 0
i = len(s) - 1
# print(i)
while i > 0:
    # print(i)
    if s[i] == "a" or s[i] == "e" or s[i] == "i" or s[i] == "o" or s[i] == "u":
        count = count + 1
    i = i - 1
print("vowel count = ", count)
