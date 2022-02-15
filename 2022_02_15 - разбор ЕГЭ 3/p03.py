with open("17.txt") as f:
    data = f.readlines()

data = list(map(int, data))

s = 0
k = 0
for x in data:
    if x % 2 == 0:
        s += x
        k += 1
sr = s/k
print(s, k, sr)

m = 0
cnt = 0
for i in range(len(data)-1):
    if (data[i]   % 3 == 0 and data[i+1] < sr) or \
       (data[i+1] % 3 == 0 and data[i] < sr):
        cnt += 1
        if data[i] + data[i+1] > m:
            m = data[i] + data[i+1]


print(cnt, m)
