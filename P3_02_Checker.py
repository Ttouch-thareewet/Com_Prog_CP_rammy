pos = input().strip()
rtrue=True
ctrue=True
r=''
cs=''
c=0
alpha='abcdefghijklmnopqrstuvwxyz'
if(len(pos)>3):
    start =0
    start = pos.find('row')+3
    start = pos.find('=',start)+1
    end =pos.find(',',start)
    if(end== -1):
        r=pos[start:len(pos)]
        r=r.strip()
    else:
        r=pos[start:end]
        r=r.strip()
        
    start =0
    start = pos.find('col')+3
    start = pos.find('=',start)+1
    end =pos.find(',',start)
    if(end== -1):
        cs=pos[start:len(pos)]
        cs=cs.strip()
    else:
        cs=pos[start:end]
        cs=cs.strip()
    if not((r>= 'a' and r <= 'z') or (r>='A' and r<='Z')):
        rtrue= False
    
    try:
        c =int(cs)
        if not(c>=1 and c<=52):
            ctrue=False
            
    except:
        ctrue=False
        
else:
    if(len(pos)==1):
        ctrue=False
    if(pos[0]>='a' and pos[0] <= 'z') or (pos[0]>='A' and pos[0]<='Z'):
        r=pos[0]
        if(len(pos)==3):
            try:
                n = pos[1]+pos[2]
                n =int(n)
                if not(n>=1 and n<=52):
                    ctrue=False
                c=n
            except:
                ctrue=False
        elif(len(pos)==2):
            try:
                n = pos[1]
                n =int(n)
                if not(n>=1 and n<=52):
                    ctrue=False
                c=n
            except:
                ctrue=False
            
    else:
        
        rtrue=False
        if(len(pos)==3):
            try:
                n = pos[1]+pos[2]
                n =int(n)
                if not(n>=1 and n<=52):
                    ctrue=False
                c=n
            except:
                ctrue=False
        elif(len(pos)==2):
            try:
                n = pos[1]
                n =int(n)
                if not(n>=1 and n<=52):
                    ctrue=False
                c=n
            except:
                ctrue=False
                
if(len(r)!=1):
    rtrue=False
if(ctrue==False and rtrue==False):
    print('Invalid row and column')
elif(ctrue==False):
    print('Invalid column')
elif(rtrue==False):
    print('Invalid row')
else:
    r =r.lower()
    i =alpha.find(r)
    if (i+c)%2==0:
        print('Black')
    else:
        print('White')