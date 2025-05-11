n =int(input())
ndept={}
for i in range(n):
    dept,num =input().split()
    ndept[dept]=int(num)
    
n =int(input())
stu =[]
for i in range(n):
    a,b,c,d,e,f =input().split()
    stu.append([a,float(b),c,d,e,f])
out =[]    
stu = sorted(stu,key = lambda x:x[1] ,reverse =True)
for i in range(n):
    for j in range(2,6):
        if(stu[i][j] in ndept ):
            if(ndept[stu[i][j]]>0):
                out.append([stu[i][0],stu[i][j]])
                ndept[stu[i][j]]-=1
                break
                
for i in sorted(out):
    print(i[0],i[1])
                