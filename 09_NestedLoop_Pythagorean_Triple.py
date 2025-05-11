def gcd(a,b):
    max=0
    min=0
    if(a>=b):
        max=a
        min=b
    if(a<=b):
        min=a
        max=b
    a=max
    b=min
    while (b!=0):
        a,b =b,a%b
    return a
def is_coprime(a, b, c):
    k =gcd(a,b)
    out = gcd(k,c)
    if(out==1):
        return True
    else:
        return False
def primitive_Pythagorean_triples(max_len):
    
    out=[]
    for i in range(1,max_len):
        for j in range(1,max_len):
            for k in range(1,max_len):
                if(i*i+j*j ==k*k):
                    temp=[i,j,k]
                    temp=sorted(temp)
                    
                    if(temp not in out and is_coprime(i,j,k)):
                        out.append(temp)
    out = sorted(out, key = lambda x:x[2])
    
    return out
exec(input().strip()) 