n, lstn, lstk = int(input()), [], []
for i in range(n):
    lstn.append(input())
k = int(input())
for j in range(k):
    s = input()
    if s.lower() not in [s.lower() for s in lstk]:
        lstk.append(s)
lower_lstk = [s.lower() for s in lstk]

for i in lstn:
    count = 0
    for j in lower_lstk:
        if j in i.lower():
            count += 1
            if count == len(lower_lstk):
                print(i)
