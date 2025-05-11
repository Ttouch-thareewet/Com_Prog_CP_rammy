n =int(input())
l1={}
l2={}
for i in range(n):
    a,b,c=input().split(' ')
    s=a+' '+b
    l1[s]=c
    l2[c]=s

n= int(input())
for i in range(n):
    f=input().strip()
    try:
        print(f+' --> '+l1[f])
    except:
        try:
            print(f+' --> '+l2[f])
        except:
            print(f+' --> '+'Not found')
