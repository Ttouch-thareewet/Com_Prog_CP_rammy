n =int(input())

uni= set()
inter=set()
for i in range(n):
    if(i==0):
        l= input().split(' ')
        l =set(l)
        uni=l
        inter =l
        continue
    l= input().split(' ')
    l =set(l)
    uni = uni.union(l)
    inter =inter.intersection(l)
    
print(len(uni))
print(len(inter))