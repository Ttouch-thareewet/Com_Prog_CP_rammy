result = input().strip()
target =int(input())
sumscore=0
unisumscore=0
place =0
k=0
result+='00000'
for i in range(1,11):
    unisumscore=0
    if result[place]<='9' and result[place]>='0':
        unisumscore +=int(result[place])
        
        if result[place+1]<='9' and result[place+1]>='0':
            unisumscore +=int(result[place+1])
            place = place+2
        elif result[place+1]=='/':
            unisumscore =10
            if result[place+2]=='X':
                unisumscore+=10
            else:
                unisumscore+=int(result[place+2])
            place = place+2
    else:
        unisumscore=10
        if result[place+1]<='9' and result[place+1]>='0':
            unisumscore +=int(result[place+1])
            if result[place+2]=='/': 
                unisumscore=20
        else:#place+1='X'
            unisumscore+=10

        if result[place+2]=='X':
            unisumscore+=10
        if result[place+2]<='9' and result[place+2]>='0':
            unisumscore+=int(result[place+2])

        place+=1

    sumscore +=unisumscore
    if target==i: 
        print(unisumscore)
        k=1

if(k==0) :
    print(sumscore)