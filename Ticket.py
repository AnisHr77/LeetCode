n=int(input("Enter the len:"))
number = int(input("Enter the number"))
r=""
k=str(number)
if (n>2):
    if n%2==0 and len(k)==n and number>0:
        for char in k :
            if char =='7' or char =='4':
                r+=char
        m=n//2
        
        b==r[m:]
        a=r[:m]
        
        r1=0
        r2=0
        for i in range (len(a)):
            r1+=int(a[i])
        for i in range (len(b)):
            r2+=int(b[i])
        if r1==r2 :
            print("YES")
        else:
            print("NO")
    else:
        print("NO")
else:
    print("NO")
    
            