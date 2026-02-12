w= 4
if(w<1 or w>100):
    print("invalid")
    
found=True    
if (w %2 !=0):
    found=False
else:
    b=((w/2 )+1)
    p=((w/2 )-1)

if (found ==False):
    print("No")
else:
    print("Yes")
    
    