n = int(input())
first = input()
in_cf = first.find("«")
out_cf = first.find("»")
if n == 1:
    print("YES")
else:
    for _ in range(n - 1):
        flag = True
        n = input()
        in_c = n.find("«")
        if n[: n.find(" ")] == first[: first.find(" ")]:
            if n[in_c + 1 : n.find("»")] > first[in_cf + 1 : out_cf]:
                flag = True
                first = n

            else:
                flag = False
                break
        else:
            if n[: n.find(" ")] > first[: first.find(" ")]:
                flag = True
                first = n
            else:
                flag = False
                break

    if flag:
        print("YES")
    else:
        print("NO")
