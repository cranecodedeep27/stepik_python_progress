n = int(input())
l = []
for i in range(n):
    d = int(input())
    l.append(d)
# print(l)

del l[1::2]
print(l)
