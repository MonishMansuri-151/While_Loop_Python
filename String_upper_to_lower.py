# 3 Convert uppercase to lowercase and lowercase to uppercase using a
# while loop.
# Input: "HeLLo" Output: "hEllO"
# Input: "JAVA" Output: "java"
s = "MOniSh"
i = 0
result = ""
while i <= len(s) - 1:
    ch = s[i]
    # print(ch)
    if ch >= "A" and ch <= "Z":
        ch = chr(ord(ch) + 32)
    elif ch >= "a" and ch <= "z":
        ch = chr(ord(ch) - 32)
    result += ch

    i = i + 1
print(result)
