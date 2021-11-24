 
 
def hod(a, b, mh, h=0):
     
     if a+b>=77:
         if h%2==1:
             return 1
         else:
             return 2
     
     h = h + 1
     
     if h > mh:
         return 3
     
     res = []
     res.append(hod(a+1, b, mh, h))
     res.append(hod(a, b+1, mh, h))
     res.append(hod(a*2, b, mh, h))
     res.append(hod(a, b*2, mh, h))
     
     if h%2==1:
         if 1 in res:
             return 1
         elif 3 in res:
             return 3
         else:
             return 2
     else:
         if 2 in res:
             return 2
         elif 3 in res:
             return 3
         else:
             return 1


for i in range(1, 69 + 1):
    print(i, hod(7, i, 2))
