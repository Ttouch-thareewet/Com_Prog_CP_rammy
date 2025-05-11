n =int(input())
k= int(input())
ktrue =True
ntrue =True
if(n<1 or n>15):
    ntrue =False
if(k<1 or k>100):
    ktrue =False
if(ntrue ==False and ktrue ==False):
    print("Invalid n and k")
    exit()
elif(ntrue ==False):
    print("Invalid n")
    exit()
elif(ktrue ==False):
    print("Invalid k")
    exit()

l1 =''
l=['0','1']
for i in range(1,k+1):
    l1+=str(i)
    if(i==k):
        if(i>9):
            for j in range(n-2):
                l1+='-'
        else:
            for j in range(n-1):
                l1+='-'
    else:
        if(i>9):
            for j in range(n-1):
                l1+='-'
        else:
            for j in range(n):
                l1+='-'
print(l1)
for i in range(2,n+1):
    c = l +l[-1::-1]
    d=c
    for j in range(1,2**i +1):
        if(j>2**(i-1)):
            d[j-1] ='1'+c[j-1]
        else:
            d[j-1] ='0'+c[j-1]
    l=d       

for i in  range(1,2**n+1):
    if(i%k!=0 ):
        if(i==2**n):
            print(l[i-1])
        else:
            print(l[i-1]+',' , end='')
         
    else:
        print(l[i-1])
    
    
    
    
    
    
    
    
    