import math


def readNumber():
    while True:
        flag = True
        number = input()
        if number[0] != "-" and number.count("-") >= 1:
            continue
        if number[0] == "." or number.count(".") > 1:
            continue
        for i in number:
            if not (i.isdigit() or i == "." or i == "-"):
                flag = False
        if flag:
            return float(number)


a = readNumber()
b = readNumber()
c = readNumber()

def printRoot(root):
    if root > 0:
        print(-math.sqrt(root), math.sqrt(root))
    elif root == 0:
        print(math.sqrt(root))


if a == 0:
    if b > 0 and c <= 0:
        print(-math.sqrt(c / b), math.sqrt(c / b))
    elif b == 0 and c == 0:
        print("ANY")
    elif b == 0:
        print("NO")
else:
    d = b * b - 4 * a * c
    if d > 0:
        root1 = (-b + math.sqrt(d)) / (2 * a)
        root2 = (-b - math.sqrt(d)) / (2 * a)
        printRoot(root1)
        printRoot(root2)
    elif d == 0:
        root1 = (-b) / (2 * a)
        printRoot(root1)
    else:
        print("NO")
