s = str(input('Please enter the string here:'))
z = 0
for vowel in s:
    if vowel == 'a':
        z = z + 1
    if vowel == 'e':
        z = z + 1
    if vowel == 'i':
        z = z + 1
    if vowel == 'o':
        z = z + 1
    if vowel == 'u':
        z = z + 1

print('Number of vowels:', z)
