namefile = input()
f = open(namefile,'r')
name = input().strip()
nsec=[]
ngender ={'F':0,'M':0}
while True:
    s =f.readline().strip()
    
    if(len(s)==0):
         
        break
    num,gender,c,sec,k =s.split(',')
    
    k =k.strip()
    sec = int(sec)
    if(k == name):
        ngender[gender]+=1
        #print(nam,name)
        if (sec not in nsec):
            nsec.append(sec)

##print(nsec)
##print(ngender)
nsec=sorted(nsec)
if(len(nsec)==0):
    print("Not found")
elif(len(nsec)==1):
    #Section: 3 --> F = 2, M = 2
    print("Section: "+str(nsec[0])+' --> '+'F = '+str(ngender['F'])+', M = '+str(ngender['M']) )
    
else:
    a=','.join([str(i) for i in nsec])
    
    print("Sections: "+a+' --> '+'F = '+str(ngender['F'])+', M = '+str(ngender['M']) )

f.close()