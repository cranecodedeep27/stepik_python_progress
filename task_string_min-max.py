max_s = "A"
min_s = "я"
while True:
    s = input()
    if s > max_s and s != "КОНЕЦ":
        max_s = s
    if s < min_s and s != "КОНЕЦ":
        min_s = s
    if s == "КОНЕЦ":
        break
print("Минимальная строка ⬇️:", min_s)
print("Максимальная строка ⬆️:", max_s)
