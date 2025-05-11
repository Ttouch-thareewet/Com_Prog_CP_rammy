def convex_polygon_area(p):
    r=0
    l=0
    s = p
    s.append(p[0])
    
    for i in range(len(s)-1):
        l+=s[i][0]*s[i+1][1]
        r+=s[i][1]*s[i+1][0]

    return  round(0.5*(abs(l-r)),1)
def is_heterogram(s):
    
    k = sorted(s.lower())

    k+= 'L'
    
    for i in range(len(k)-1):
       if(k[i]==k[i+1] and 'a'<=k[i]<='z'):
          return False
    return  True
def replace_ignorecase(s, a, b):
    s2 =s
    out=s
    s2=s2.lower()
    a2 =a
    a2 =a2.lower()
    start = 0
    while s2.find(a2,start)!=-1:
        k= s2.find(a2,start)
        # abcdefgh
        # abcabcfgh
        # 01234567
        # ---k
        
        out = out[0:k]+b+out[k+len(a):]
        s2 = out.lower()
        
        start = k+len(b)
    
    return out

def top3(votes):
    a=[]
    for key in sorted(votes.keys()):
        a.append([-votes[key],key])
    
    a=sorted(a)
    out =[]
    if(len(a)>3):
        
        for i in range(3):
            out.append(a[i][1])
        return out
    else:
        for i in range(len(a)):
            out.append(a[i][1])
        return out



for k in range(2):
   exec(input().strip())
