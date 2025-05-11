c = input().split()
a=input()


n2 = int((len(c))/2)
for i in range(len(a)):
    

    if(a[i]=="C"):
        temp = c[n2:n2*2]
        for j in range(n2):
            temp.append(c[j])
        c=temp
    elif(a[i]=="S"):
        temp=[]
        temp1=c[0:n2]
        temp2=c[n2:n2*2]
        for j in range(n2):
            temp.append(temp1[j])
            temp.append(temp2[j])
        c=temp    

for e in c:
    print(e,end =" ")      


