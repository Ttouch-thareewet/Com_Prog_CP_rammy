n = int(input()) 
v=[]
for i in range(n):
    k =input().split()
    v.append(k)

c = input().split() 
if c[0] == 'show' :
    for i in range(n):
        print(" ".join(v[i]))
        
        
elif c[0] == 'max' :
    m =0.0
    t=int(c[1])
    
    v=sorted(v)
    for i in range(n):
        # print(float(v[i][t]))
        if(float(v[i][t]) >= m):
            m =float(v[i][t])
    
    for i in range(n):
        if(m ==float(v[i][t])):
            print(v[i][0]+' '+str(m))
            exit()
            
elif c[0] == 'avg' :
    sum=0.0
    t=int(c[1])
    v=sorted(v)
    for i in range(n):
        sum+=float(v[i][t])
    print(round(sum/n,4))
    # print(sum/n)
elif c[0] == 'get' :
    for i in range(n):
        if(c[1]==v[i][0]):
            for j in v[i]:
                print(j+' ',end='')
            exit()
    print(c[1]+' not found')    
elif c[0] == 'sort' :
    t =int(c[1])
    for i in range(n):
       
        v[i].insert(0,v[i][t])
    v=sorted(v)
    for i in range(n):
        print(v[i][1]+' ',end='')