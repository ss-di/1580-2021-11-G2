

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
ans = []

for i in range(3, int(88_888_888**0.25)+2, 2):
    if  r[i]:
        j = i**4
        while j <= 88_888_888:
            if j >= 77_777_777:
                print(j, i)
                ans.append((j, i))
            j *= 2

ans.sort()
print(ans)
