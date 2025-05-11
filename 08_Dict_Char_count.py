s = input().strip()
s= s.lower()

count ={}
for i in range(len(s)):
    if 'a'<=s[i]<='z':
        try:
            count[s[i]]+=1
        except:
            count[s[i]]=1
# for i in range(len(s)):
#     count[s[i]]=0
# for i in range(len(s)):
#     count[s[i]]+=1

c=[]
for i in count:
    c.append([-1*count[i],i])

c.sort()

for i in range(len(c)):
    print(c[i][1]+' -> '+str(-1*c[i][0]))