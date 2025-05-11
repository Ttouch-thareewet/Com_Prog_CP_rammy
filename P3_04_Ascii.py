filename =input().strip()
fu =input().strip()
f = open(filename,'r')
l=[]
out=[]
n=0
while (True):
    s =f.readline().strip()
    if(len(s)==0):
        break
    l.append(s)
    n+=1
for i in range(len(l[0])):
    dot =True
    for j in range(len(l)):
        if(l[j][i]!='.'):
            dot=False
        
    if(dot==True):
        out.append(i)
if(fu=='LSTRIP'):
    outl=[]
    for i in range(len(out)-1):
        if(out[i+1]-out[i]!=1):
            outl.append(out[i])
            break
        outl.append(out[i])
    for i in range(len(l)):
        for j in range(len(l[0])):
            if(j not in outl):
                print(l[i][j],end='')
        print("")
elif(fu=='RSTRIP'):
    outl=[]
    for i in range( len(out)-1):
        if(i==0):
            d=0
        elif(out[-i-1]-out[-i]!=-1):
            
            break
        outl.append(out[-i-1])
    for i in range(len(l)):
        for j in range(len(l[0])):
            if(j not in outl):
                print(l[i][j],end='')
        print("")
elif(fu=='STRIP'):
    outl=[]
    for i in range(len(out)-1):
        if(out[i+1]-out[i]!=1):
            outl.append(out[i])
            break
        outl.append(out[i])
    for i in range( len(out)-1):
        if(i==0):
            d=0
        elif(out[-i-1]-out[-i]!=-1):
            
            break
        outl.append(out[-i-1]) 
    for i in range(len(l)):
        for j in range(len(l[0])):
            if(j not in outl):
                print(l[i][j],end='')
        print("")
    
elif(fu=='STRIP_ALL'):
    for i in range(len(l)):
        for j in range(len(l[0])):
            if(j not in out):
                print(l[i][j],end='')
        print("")
else:
    print('Invalid command')