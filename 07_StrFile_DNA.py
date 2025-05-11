DNA = input().strip()

func = input().strip()
if func=='D':
    try:
    
        samechar =input().strip()
     
    except:
        pass



d = ['A','T','C','G']
DNA = DNA.upper()
for i in range(len(DNA)):
    if(DNA[i] not in d):
        print('Invalid DNA')
        exit()

if(func=='R'):
    dna =[]
    for i in range(len(DNA)):
        if(DNA[i]=='A'):
            dna.append('T')
        elif(DNA[i]=='T'):
            dna.append('A')
        elif(DNA[i]=='C'):
            dna.append('G')
        else:
            dna.append('C')
    for i in range(len(dna)):
        print(dna[(-i)-1],end='')

if(func=='F'):
    key = {'A':0,'C':0,'T':0,'G':0}
    for c in DNA:
        key[c]+=1
    
    A= 'A='+str(key['A'])+', '
    T= 'T='+str(key['T'])+', '
    G= 'G='+str(key['G'])+', '
    C= 'C='+str(key['C'])
    print(A+T+G+C)

if(func=='D'):
    start=0
    count =0
    
    while True:
        if(DNA.find(samechar,start)!=-1):
            count+=1
            start =DNA.find(samechar,start)+1
        else:
            print(count)
            break

