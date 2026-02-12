


def Team(n:int , l:list[int])-> int : 
    n=len(l)
    count=0
    if not l ==[]:
        for c in l :
            k=str(c)
            if(k.count("1")>=2) : 
                count+=1
        return count  
    else:
        return 0       

Team()    