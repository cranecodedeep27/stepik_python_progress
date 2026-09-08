n = int(input())
first_d = int(input())
l = []
for i in range(1, n):
    d = int(input())
    l.append(d + first_d)
    first_d = d
print(l)
