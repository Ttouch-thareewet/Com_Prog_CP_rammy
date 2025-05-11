def total(pocket):
    total=0
    for i in sorted(pocket, reverse=True):
        total+= i*pocket[i]
    return total
def take(pocket, money_in):
    for i in money_in:
        try:
            pocket[i]+=money_in[i]
        except:
            pocket[i]=money_in[i]
    return pocket

def pay(pocket, amt):
    if(amt>total(pocket)):
        return {}
    p={}
    now = amt
    for i in sorted(pocket,reverse=True):
        if(now<i):
            
            continue
        else:
            
            k=int(now/i)
            if k>pocket[i]:
                now -=i*pocket[i]
                p[i]=pocket[i]
                pocket[i]=0
            else:
                now-= i*k
                p[i]=k
                pocket[i]-=k
    
    if(now==0):
        return p
    else:
        return {}
     
       
exec(input().strip()) 