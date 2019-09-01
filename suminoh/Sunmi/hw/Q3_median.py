def median(x):
    x = sorted(x)
    if len(x) % 2 == 1:
        a = len(x) // 2
        med = x[a]
    else:
        a = len(x) // 2
        med = (x[a - 1] + x[a]) / 2
    return med
    