def printXY(number):
    x = -(number - 1)
    y = -(number - 1)
    while y < number:
        while x < number:
            print str(number-max((abs(x)),abs(y))),
            x += 1
        print ""
        x = -(number - 1)
        y += 1
printXY(4)