# Given a string, check if it is a palindrome using a while loop.
str = "MaaM"
empt = ""
i = len(str) - 1
while i >= 0:
    empt += str[i]
    i = i - 1
print(empt)
if empt == str:
    print("palindrome string ")
else:
    print("not plindrome string !")
