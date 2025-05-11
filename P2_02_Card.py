s = input()
n = int(len(s)/2)
f1 ={'A':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'T':10,'J':11,'Q':12,'K':13}
f2 ={'C':1,'D':2,'H':3,'S':4}
for i in range(n-1):
    a = f1[s[i*2]]
    b=f2[s[i*2+1]]
    c = f1[s[i*2+2]]
    d=f2[s[i*2+3]]
    if(a==c):
        d=b-d
    else:
        d=a-c
    if(d>0):
        print('+'+str(d),end='')
    elif(d<0):
        print(str(d),end='')
    else:
        print("0",end='')