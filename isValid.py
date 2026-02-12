
def isValid( s: str) -> bool:
    dict1={ "(":")" , "{":"}" , "[":"]"}
    stack = []
    boolean=False
    for c in s:
            if c in dict1 :
                stack.append(c)
            if c in dict1.values():
                for k,v in dict1.items():
                    if v==c :
                        l=k
    
                        checks=stack.pop()
                        if checks == l:
                            boolean = True
                        else:
                            boolean = False
            
                    
    return boolean               
print(isValid("({{{{}}}))"))
        

stack =["{","}"]
stack.pop()
print(stack)