map={}
station=[]
start=''
out=[]
while True:
    s=input()
    a =s.split()
    if(len(a)==1):
        station.append(a)
        start=a[0]
        break
    s1 = a[0]
    s2 =a[1]
    station.append(a[0])
    station.append(a[1])
    
    if(s1 not in map):
        map[s1]= [s2]
    else:
        map[s1].append(s2)
    if(s2 not in map):
        map[s2]= [s1]
    else:
        map[s2].append(s1)
    
if(start not in map):
    print(start)
    exit()

for i in range(len(map[start])):
    out.append(map[start][i])
    for j in range(len(map[map[start][i]])):
        out.append(map[map[start][i]][j])
  
out.append(start)      
out =set(out)
out =list(out)
out =sorted(out)
for i in out:
    print(i)