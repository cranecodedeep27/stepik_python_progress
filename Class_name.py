n = int(input())
for i in range(n):
    clasc = input()
    if len(clasc) == 2 and clasc[0] in "1234567890" and clasc[1] in "АБВГДЕЖЗИЙКЛМНОП":
        print("YES")
    else:
        print("NO")
    