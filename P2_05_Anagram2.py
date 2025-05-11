s1 =input()
s2 =input()
counts1={}
counts2={}
counts3={}
copys1=s1
copys2=s2
s1=s1.lower()
s2=s2.lower()
outs1=[]
outs2=[]

s3=s1+s2
s3 = sorted(s3)
for i in range(len(s3)):
    if('a'<= s3[i]<='z'):
        counts1[s3[i]] =0
        counts2[s3[i]]=0
        counts3[s3[i]]=0
     
for i in s1:
    if('a'<=i<='z'):
        counts1[i]+=1
for i in s2:
    if('a'<=i<='z'):
        counts2[i]+=1

for c in sorted(counts3):
    if(counts1[c]>counts2[c]):
        if(counts1[c]-counts2[c]==1):
            outs1.append(' - remove '+str(counts1[c]-counts2[c])+' '+c)
        else:
            outs1.append(' - remove '+str(counts1[c]-counts2[c])+' '+c+"'s")
    elif(counts2[c]>counts1[c]):
        if(counts2[c]-counts1[c]==1):
            outs2.append(' - remove '+str(counts2[c]-counts1[c])+' '+c)
        else:
            outs2.append(' - remove '+str(counts2[c]-counts1[c])+' '+c+"'s")
    

if(len(outs1)==0):
    outs1.append(' - None')
if(len(outs2)==0):
    outs2.append(' - None')

print(copys1)
for i in outs1:
    print(i)
print(copys2)
for i in outs2:
    print(i)