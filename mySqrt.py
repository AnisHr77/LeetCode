def addBinary(a: str, b: str) -> str:
        carry=0
        resultstr=""
        while (len(a)>len(b)):
            b="0"+b
        while (len(a)<len(b)):
            a="0"+a
        while(len(a)>0):
            if(len(a)>0):
                bit=int(a[-1:])+int(b[-1:])+carry
                a=a[:-1]
                b=b[:-1]
                if bit==3:
                    resultstr="1"+resultstr
                    carry=1
                    
                elif bit == 2:
                    resultstr="0"+resultstr
                    carry=1
                    
                elif bit==1:
                    resultstr="1"+resultstr
                    carry=0
                else:
                    resultstr="0"+resultstr
                    carry=0
            if(len(a)==0 and carry>0):
                resultstr="1"+resultstr    
            
        resultstr=int(resultstr)
        return resultstr

print(addBinary("111", "100"))

"""a="10046"
b="1005"
while (len(a)>len(b)):
    b="0"+b
while (len(a)<len(b)):
    a="0"+a
    
print(b)
while(len(a)>0):
    bit=int(a[-1:])+int(b[-1:])
    print(bit)
    a=a[:-1]
    b=b[:-1]
"""