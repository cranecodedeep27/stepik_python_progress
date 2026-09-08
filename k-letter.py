n = int(input())
l = []
for i in range(n):
    s = input()
    l.append(s)
# print(l)
k = int(input())
for i in range(len(l)):
    if len(l[i]) < k:
        continue
    print(l[i][k - 1], end="")
