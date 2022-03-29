def f(x, a, r):
    return not ((x & 108 == 0) or (x & 60 == 0)) or (x & a == 0) or (x & r == 0)

def check(r):
    for x in range(1000):
        for a in range(1000):
            if not f(x, a, r):
                return False
    return True

cnt = 0
for r in range(1, 1000):
    if check(r):
        cnt += 1
    
print(cnt)
