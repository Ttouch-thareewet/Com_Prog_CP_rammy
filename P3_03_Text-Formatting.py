filename = input().strip()
f = open(filename,'r')
n =int(input())
for i in range(1,n+1):
    if(i%10==0):
        print(str(i//10),end='')
    else:
        print('-',end='')
l =[]
print('')
s=''
k=0
while(True):
    s1 = f.readline().strip()
    if(len(s1)==0):
        s+='.'
        break
    if(k==0):
        s +=s1
        k=1
    else:        
        s = s+'.'+s1
s+='.'


dotl=[]
wordl=[]
tempw=''
tempd=''
for i in range(len(s)-1):
    if(s[i]=='.'):
        tempd+='.'
        if(s[i+1]!= '.'):
            dotl.append(tempd)
            tempd=''
    else:
        tempw+=s[i]
        if(s[i+1]=='.'):
            wordl.append(tempw)
            tempw=''
    
dotl.append('.')
s=''
for i in range(len(wordl)):
    copys1 =s
    copys2 =s
    copys1+= wordl[i]
    copys2+= wordl[i] +dotl[i]
    
    if(i == len(wordl)-1):
        if(len(wordl[i])>n):
            print(s.strip('.'))
            s=''
            print(wordl[i])
        elif(len(copys1)>n):
            print(s.strip('.'))
            s=''
            print(wordl[i])
        else:
            print(copys1.strip())
    else:
        if(len(wordl[i])>n):
            print(s.strip('.'))
            s=''
            print(wordl[i])
            continue
        if(len(s)>n):
            print(s.strip('.'))
            s=''
            s=wordl[i]+dotl[i]
        elif(len(copys1)>n):
            print(s.strip('.'))
            s=wordl[i]+dotl[i]
        else:
            s= copys2
        
    
    

    
