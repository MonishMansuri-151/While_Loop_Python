# Problem: Given a string, count uppercase and lowercase letters separately.
s = "hello wOlD"
i = 0
upper = 0
lower = 0
while i <= len(s) - 1:
    if s[i] >= "A" and s[i] <= "Z":
        # print(s[i])
        upper += 1
    else:
        # print(s[i])
        lower += +1
    i = i + 1
print("UPPER CASE = ", upper)
print("Lower Case = ", lower)
