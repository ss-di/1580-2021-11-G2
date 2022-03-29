cnt = 0

def hod (a, b, h, mh, put=''):
    global cnt
    if a >= 50 or b >= 50:
        if h % 2 == 1:
            if (a + b <= 109) else 2) == 2: cnt +=1
            return (1 if (a + b <= 109) else 2, put)
        else:
            if (2 if (a + b <= 109) else 1) == 2: cnt +=1
            return (2 if (a + b <= 109) else 1, put)
    h += 1
    if h > mh:
        return (3, put)
    res = []
    
    res.append(hod(a + 1, b, h, mh, put + 'A'))
    res.append(hod(a + 2, b, h, mh, put + 'B'))
    res.append(hod(a * 2, b, h, mh, put + 'C'))
    res.append(hod(a, b + 1, h, mh, put + 'a'))
    res.append(hod(a, b + 2, h, mh, put + 'b'))
    res.append(hod(a, b * 2, h, mh, put + 'c'))
    
    if h % 2 == 1:
        for r in res:
            if r[0] == 1:
                return r
        for r in res:
            if r[0] == 3:
                return r
        return res[0]
    else:
        for r in res:
            if r[0] == 2:
                return r
        for r in res:
            if r[0] == 3:
                return r
        return res[0]
'''
for a in range(1, 20+1):
    print(a, hod(a, 0, 5))

'''
'''
print("", end = "\t")
for h in range(1, 7):
    print(h, end="\t")
print()
for a in range(1, 49+1):
    print(a, end = "\t")
    for h in range(1, 7):
        print(hod(24, a, 0, h), end="\t")
    print()
'''

hod(24, 21, 0, 4)
print(cnt)
