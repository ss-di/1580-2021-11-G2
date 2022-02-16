def calc(x, mult):
    if x == 11:
        return 1
    if x > 11:
        return 0
    res = 0
    res += calc(x+1, False)
    res += calc(x+2, False)
    if not mult:
        res += calc(x*2, True)
    return res

print(calc(1, False))
