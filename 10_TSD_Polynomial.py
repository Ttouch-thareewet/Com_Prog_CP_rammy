def add_poly(p1, p2):
    out=[]
    k={}
    for i in p1:
        if(i[1]in k):
            k[i[1]]+=i[0]
        else:
            k[i[1]] =i[0]
    for i in p2:
        if(i[1]in k):
            k[i[1]]+=i[0]
        else:
            k[i[1]] =i[0]
    d=[]
    for key,value in k.items():
        d.append((key,value))
        
    g = sorted(d ,reverse =True)
    for i in g:
        if(i[1]!=0):
            out.append((i[1],i[0]))
        
    return out
def mult_poly(p1, p2):
    out=[]
    k={}
    for i in p1:
        for j in p2:
            if(i[1]+j[1] in k):
                k[i[1]+j[1]]+=i[0]*j[0]
            else:
                k[i[1]+j[1]]=i[0]*j[0]
    d=[]
    for key,value in k.items():
        d.append((key,value))
        
    g = sorted(d ,reverse =True)
    for i in g:
        if(i[1]!=0):
            out.append((i[1],i[0]))
        
    return out
for i in range(3):
    exec(input().strip())