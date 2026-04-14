# 📝 Problem: Given a sentence, print each word reversed (words separated by space).
string = "hello world"  # create a string
temp = ""
result = ""
i = 0
while i <= len(string) - 1:
    if string[i] != " ":
        temp += string[i]
    else:
        j = len(temp) - 1
        while j >= 0:
            result += string[j]
            j = j - 1
        # print(result)
        result += " "
        # print(result)
        temp = ""
    i = i + 1
j = len(temp) - 1
while j >= 0:
    result += temp[j]
    j = j - 1
print(result)
