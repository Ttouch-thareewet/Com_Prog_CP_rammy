n =int(input())
s=[]
c=[]
for i in range(n):
    id,a= input().split(":")
    l=set(a.split(","))
    s.append([id,l])
    c.append(id)
f = input()
j = c.index(f)
se =s[j][1]
d=[]
for i in range(n):
    if(f!=s[i][0]):
        out = se.intersection(s[i][1])
        if(len(out)!=0):
            d.append(s[i][0])
    
if(len(d)==0):
    print('Not Found')
else:
    for i in d:
        print(i)