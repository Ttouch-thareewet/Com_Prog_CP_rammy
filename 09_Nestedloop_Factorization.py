def factor(N):
    out =[]
    n=N
    for i in range(2,N+1):
        k=0
        while(True):
            if(n==1):
                if(k!=0):
                    out.append([i,k])
                return out
            if(n%i==0):
                n =n//i
                k+=1
            else:
                break
             
        if(k!=0):
            out.append([i,k])
            
    
        
exec(input().strip()) 