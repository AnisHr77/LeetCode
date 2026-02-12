def Broze(s:str)-> str :
    out=""
    l=s.split(".")
    for c in l :
        indice = str(len(c))
        out+=indice
               
                
    return out

print(Broze("-.--."))