

def check (x):
    '''    for i in range(2, int(x**0.5)+2):
        if x % i == 0:
            return False
    '''
    i = 2
    while i*i <= x:
        if x % i == 0:
            return False
        i += 1
    return True


r = [True] * (4_000_000+1)

r[0] = r[1] = False

for i in range(2, 4_000_000):
#    if i%1000 == 0:
#        print(i)
    if r[i]:
        for j in range(i*i, 4_000_000+1, i):
            r[j] = False

for i in range(3532000, 3532160+1):
    if check(i):
        print(i)

