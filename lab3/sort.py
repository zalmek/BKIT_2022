print(sorted([4, -30, 30, 100, -100, 123, 1, 0, -1, -4], key=abs, reverse=True))
print(sorted([4, -30, 30, 100, -100, 123, 1, 0, -1, -4], key=lambda a: abs(a), reverse=True))
