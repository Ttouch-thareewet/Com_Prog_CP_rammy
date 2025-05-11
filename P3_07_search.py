l =[]

n = int(input())
for i in range(n):
    name=input()
    sentence =input()
    numberwords = len(sentence.split())
    numberwordss = len(set(sentence.split()))
    
    l.append([name,sentence,numberwords,numberwordss])
    
key =input()
while(key!= '-1'):
    ma =[]
    
    for i in range(n):
        word =l[i][1].split()
        m=0
        for j in range(len(word)):
            if(key ==word[j]):
                m+=1
        
        ma.append(m/l[i][2] *1/l[i][3])
    max=0
    out=0
    for i in range(n):
        if(max<ma[i]):
            out=i
            max=ma[i]
    if(max==0):
        print('NOT FOUND')
    else:
        print(l[out][0])
    key =input()
    