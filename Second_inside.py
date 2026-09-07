s = input()
count = 0
first_inside = s.find("f")
second_inside = s[first_inside + 1 :].find("f")
for i in range(len(s)):
    if s[i] == "f":
        count += 1
if count == 1:
    print("-1")
elif count == 0:
    print("-2")
else:
    print(second_inside + first_inside + 1)
