import math


def readNumber():
    """Checks if provided string is float number. \n
        Time complexity - O(n),\nn  = length of string
        """
    while True:
        flag1 = False
        number = input()
        flag2 = False
        if number[0] == "-" and len(number) > 1:
            flag1 = True
        elif not number[0].isdigit():
            continue
        i = 1
        while i < len(number):
            if number[i] == ".":
                if flag2:
                    break
                flag2 = True
            elif number[i] == "-":
                if flag1:
                    break
                flag1 = True
            elif not number[i].isdigit():
                break
            i += 1
        if i == len(number):
            return float(number)


def exception_readNumber():
    """Checks if provided string is float number by handling exception."""
    while True:
        try:
            return float(input())
        except:
            continue


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
