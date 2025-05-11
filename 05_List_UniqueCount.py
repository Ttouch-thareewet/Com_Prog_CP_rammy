num = input().split()
for i in range(len(num)):
    num[i]=int(num[i])
num.sort()
count =1
l=[]
l.append(int(num[0]))
for i in range(len(num)-1):
    if(num[i]!=num[i+1]):
        count +=1
        l.append(int(num[i+1]))

print(count)

if len(l)>=10:
    print(l[0:10])
else :
    print(l)
