t = input()
n=int(input())
s=[""]*n
k=0
a=""
for i in range (n):
    s[i]=input().strip()
    
for i in range (n):
    if(len(s[i])!=len(s[0])and k==0):
        print("Invalid size")
        k =1
for i in range (n):
    a+=s[i].strip()

l =len(s[0])
if(k==0):
    if(t=='90'):
        for i in range(l):
            print(a[(-1*l)+i::-l])
    elif(t=="180"):
        
        for i in range(1,n*l+1):
            print(a[-i],end="")
            if(i%l==0):
                print("")           
    elif(t=="flip"):
        for i in range(n):
            for j in range(l):
                print(s[i][-j-1],end="")
            print("")

