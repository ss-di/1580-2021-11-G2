 
 
a = 2**5-1-2**1-2**3
 
for x in range(0, 255):
    if not((x & a == 0) or ((x & 20 != 0) or (x & 5 != 0))):
        print(bin(x), x)
 

print(bin(a), a)


# x&a==0 or x & 20 != 0 or x & 5 != 0
# 10100
# 00101
# 10101


