h= int(input())
for i in range(h-1):
    for j in range(h-i-1):
        print(".",end="")
    if(i==0):
        print("*")
    else :
        print("*",end="")

    for j in range((2*i)-1):
        print(".",end="")
    
    if(i!=0):
        print("*")
    
        

for i in range((2*h)-1):
    print("*",end="")
        