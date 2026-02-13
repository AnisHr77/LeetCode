def mySqrt(x: int) -> int:
        if x==0 :
            return 0 
        n=x//2 
        i=1   
        while i*i < x:
                i+=1
        if(i*i>x):
             i-=1
        return i
print(mySqrt(10))    