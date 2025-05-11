func=''
data =[]
s3={}
k3={}
while(True):
    i = input()
    if(len(i)==1):
        func=i
        break
    a,b,c = i.split()
    k3[b]=0
    c=int(c)
    if(a+' '+b not in s3):
        s3[a+' '+b]=c
    else:
        s3[a+' '+b]+=c
    data.append([a,b,c])
    
if(func=='1'):
    out ={}
    for i in range(len(data)):
        if(data[i][1] not in out):
            out[data[i][1]] = -data[i][2]
        else:
            out[data[i][1]] += -data[i][2]
    k =sorted(out.items(),  key = lambda  x:x[1])
    a = ', '.join([k[0][0],k[1][0],k[2][0]])
    print(a)
elif(func=='2'):
    out ={}
    d =[]
    for i in range(len(data)):
        if(data[i][0]+' '+data[i][1] in d):
            continue
        if(data[i][1] not in out):
            out[data[i][1]] = -1
            d.append(data[i][0]+' '+data[i][1])
        else:
            out[data[i][1]] += -1
            d.append(data[i][0]+' '+data[i][1])
    k =sorted(out.items(),  key = lambda  x:x[1])
    a = ', '.join([k[0][0],k[1][0],k[2][0]])
    print(a)
elif(func=='3'):
    out ={}
    k={}
    
    for key,value in s3.items():
        ota,idol = key.split()
        if(ota in out):
            out[ota].append([-value,idol])
        else:
            out[ota] =[[-value,idol]]
        
    for key in out.keys():
        
        temp = out[key]
        temp = sorted(temp)
        
        no1 = temp[0][1]
        k3[no1]+=1
    m = sorted(k3.items(),key = lambda x:x[1],reverse =True)
    a = ', '.join([m[0][0],m[1][0],m[2][0]])
    print(a)

    