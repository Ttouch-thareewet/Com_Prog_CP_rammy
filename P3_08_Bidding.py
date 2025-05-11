n = int(input())
info ={}
product ={}# {namep nameb :[priceb,-i]} ตอนเสิชโพรดักเสิชมากสุด ,reverse=True
winfo ={}# { namew :[product1,product2]}
listname =[]
l ={}#{ namep :[[price,-i,nameb]]}
for i in range(n):
    s = input().strip().split()
    if(s[0]!='B' and s[0] !='W'):
        continue
    if(len(s)==3):
        if s[1] not in winfo.keys():
            winfo[s[1]] =[s[2]]
        else:
            winfo[s[1]].append(s[2])
        listname.append(s[1])
    elif(len(s)==4):
        nameb=s[1]
        f = -i 
        namep=s[2]
        listname.append(nameb)
        priceb =int(s[3])
        product[namep+' '+nameb]=[priceb,n-i]



for namew,listproductw in winfo.items():
    for pro in listproductw:
        if(pro+' '+namew in product.keys() ):
            temp =product[pro+' '+namew][1]
            product[pro+' '+namew] =[-1,0]

for key,listprice in product.items():
    namep,nameb = key.split()
    if(listprice[0]==-1):
        continue
    if(listprice[1]==0):
        continue
    if(namep not in l.keys()):
        
        l[namep]=[[listprice[0],listprice[1],nameb]]
    else:
        l[namep].append([listprice[0],listprice[1],nameb])
        
for namep,lists in  l.items():
    temp = sorted(lists,key = lambda x:(x[0],x[1]),reverse=True)
    l[namep] =temp
    
#already sort

out ={}#{nameb :{'sum'=price,'product'=[product]}}
for namep,lists in l.items():
    p = lists[0][0]
    nameb = lists[0][2]
    if(nameb not in out):
        out[nameb]={'sum':p,'product':[namep]}
    else:
        out[nameb]['sum']+=p
        out[nameb]['product'].append(namep)
listname =set(listname)
listname =list(listname)
listname = sorted(listname)
for i in listname:
    if(i not in out):
        print(i+': $0')
    else:
        out[i]['product'] = sorted(out[i]['product'])
        print(i+ ': $'+str(out[i]['sum'])+' -> '+' '.join(out[i]['product']))


    
    
    
    
    
    
    
    