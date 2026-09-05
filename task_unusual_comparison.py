s1, s2 = input(), input()
s1, s2 = s1.lower(), s2.lower()
alphabet = "abcdefghijklmnopqrstuvwxyzйцукенгшщзхъфывапролджэячсмитьбюё"
s_1, s_2 = "", ""

for i in range(len(s1)):
    if s1[i] in alphabet:
        s_1 += s1[i]

for x in range(len(s2)):
    if s2[x] in alphabet:
        s_2 += s2[x]

if s_1 == s_2:
    print("YES")
else:
    print("NO")
