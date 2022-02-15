F = [0]*1000000000

F[0] = 0
cnt = 0
for i in range(1, 1000000000):
    if i % 100000 == 0:
        print(i)
    if i % 2 != 0:
        F[i] = F[i-1]+1
    else:
        F[i] = F[i//2]
    if F[i] == 2:
        cnt += 1
        
print(F.count(2))
print(cnt)
