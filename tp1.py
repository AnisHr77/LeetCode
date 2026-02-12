


n=int(input("Donner le nombre probleme: "))
M=[]
for i in range(n):
    l=int(input(f"Donner le {i} elem de matrice :"))

    M.append(l)
      
def Team(n:int , M:list[int]) -> int :
    count=0
    h=len(M)
    
    if not M==[] and h==n :
        
        for c in M:
            k=str(c)
            
            
            if(k.count('1')>=2):
                count+=1
        return count
    else:
        return 0


print(Team(n,M))

