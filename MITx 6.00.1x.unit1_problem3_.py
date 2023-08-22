s = str(input('Please enter the string here:'))
current = ''
longest = ''
for x in range(len(s)):
    if (s[x] >= s[x - 1]):
        current += s[x]
    else:
        current = s[x]
    if len(current) > len(longest):
        longest = current
print("Longest substring in alphabetical order is: ", longest)