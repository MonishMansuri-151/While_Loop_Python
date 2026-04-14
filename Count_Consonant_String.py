# Problem: Given a string, count the number of consonants (letters that are not vowels a,e,i,o,u).
str = " hello bagru"
i = 1
count = 0
while i <= len(str) - 1:
    # print(str[i])
    if (
        str[i] != "a"
        and str[i] != "e"
        and str[i] != "i"
        and str[i] != "o"
        and str[i] != "u"
    ):
        count += 1
    i = i + 1
print("consonant count => ", count)
