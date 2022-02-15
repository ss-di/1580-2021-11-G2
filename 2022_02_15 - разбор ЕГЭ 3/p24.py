with open("24.txt") as f:
    data = f.readline()

'''
data = data.split('E')

cnt = 0
for i in range(1, len(data) - 1):
    if len(data[i]) >= 12-2 and 'F' not in data[i]:
        cnt += 1

print(cnt)
'''

posE = []
cnt = 0
for i in range(len(data)):
    if data[i] == 'E':
        posE.append(i)

for i in range(len(posE)-1):
    if posE[i+1] - posE[i] >= 12 - 1 and 'F' not in data[posE[i]:posE[i+1]+1]:
        cnt += 1;

print(cnt)
