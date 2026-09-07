a, b, c, d = input(), input(), input(), input()
big_d = max(a, b, c, d)
small_d = min(a, b, c, d)
print((ord(big_d[-1]) * ord(small_d[-1])) ** 2)
