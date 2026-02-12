def translation (s:str , t:str):
    s=s.strip()
    s=s.lower()
    t=t.strip()
    t=t.lower()
    
    reversedS= s[::-1]
    if(t==reversedS):
        print("yes")
    else:
        print("No")
    
translation("code", "code")    
    
