n =int(input())
info ={}
for i in range(n):
    a,b,c,d =input().split()
    info[a]={'group':b,'year':c,'department':d}
    
output =[]
out= input().split()
specific ={}
n =len(out)
for word in out:
    if(word=='Dog'):
        specific['group']= word
        continue
    if(len(word)>1):
        if( 'A'<=word[0]<='Z'):#depart
            specific['department'] =word
        else:
            specific['year'] =word
    else:
        specific['group']= word
s=[]        
for key,value in info.items():
    check = True
    for key2,value2 in specific.items():
        if(specific[key2]!=info[key][key2]):
            check= False
            break
    if(check==True):
        s.append(key)
            
if(len(s)==0):
    print('Not Found')
else:
    s=sorted(s)
    for name in s:
        print(name+' '+info[name]['group']+' '+info[name]['year']+' '+info[name]['department'])
        
    