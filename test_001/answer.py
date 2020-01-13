def Calculate(x):
    w = 5832
    for i in range(x):
        w -= w/3
    return w

y = Calculate(2)
print(y)