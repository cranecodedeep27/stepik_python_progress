n = int(input())
s = input()

for i in range(len(s)):

    c = ord(s[i]) - n

    if c < 97:
        c = 122 - (96 - c)
    print(chr(c), end="")
