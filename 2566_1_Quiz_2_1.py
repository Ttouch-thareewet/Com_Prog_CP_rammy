num = input().split()

num = [int(x) for x in num]
num =sorted(num)

if(len(num)%2==0):
    n=len(num)
    if(n%4==0):
        nq1 = n//4-1
        nq3= 3*n//4-1
        
        q1= num[nq1]/2+num[nq1+1]/2
        q3= num[nq3]/2+num[nq3+1]/2
    else:
        
        nq1 = n//4 
        nq3 =3*n//4 
        q1=num[nq1]
        q3=num[nq3]
       
    
    
else:
    n=len(num)
    if(n%4==3):
       nq1=n//4
       nq3=3*n//4
       q1=num[nq1]
       q3=num[nq3]
    else:
        nq1=n//4-1
        nq3=3*n//4
        #print(nq1)
        #print(nq3)
        q1=num[nq1]/2+num[nq1+1]/2
        #print(q1)
        q3=num[nq3]/2+num[nq3+1]/2
        #print(q3)
iqr =q3-q1
l =q1-1.5*iqr
#L = 3.5 U = 7.5
u =q3+1.5*iqr
print("L = "+str(l)+" U = "+str(u))
out=[]
for i in num:
    if(i<l or i>u):
        out.append(i)
if(len(out)==0):
    print("Not found")
else:
    print(" ".join([str(x) for x in out]))