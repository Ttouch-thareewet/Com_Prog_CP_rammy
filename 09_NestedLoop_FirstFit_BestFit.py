def first_fit(L, e): 
    k=0
    for i in  range(len(L)):
        if(sum(L[i])+e <=100):
            k=1
            L[i].append(e)
            break
    if(k==0):
        L.append([e])
         
def best_fit(L, e):
    max =0
    
    for i in range(len(L)):
        
        if(sum(L[i])+e >= max and sum(L[i])+e<=100):
            max= sum(L[i])+e
    for i in range(len(L)):
        if(sum(L[i])+e==max):
            L[i].append(e)
    if(max==0):
        L.append([e])
            
def partition_FF(D):
    out =[]
    for i in range(len(D)):
        first_fit(out,D[i])
    return out
def partition_BF(D):
    out =[]
    for i in range(len(D)):
        best_fit(out,D[i])
    return out
exec(input().strip()) 