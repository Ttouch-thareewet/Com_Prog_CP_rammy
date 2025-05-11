namefile =input()
f =open(namefile,'r')
func = f.readline().strip()
text = f.readline().strip()
if(func=='T2M'):
    while(True):
        s =f.readline().strip()
        out=''
        k=1
        if(len(s)==0):
            exit()
        for i in range(len(s)):
            start = text.find(s[i])
            if(start==-1):
                print('Invalid : '+s)
                k=0
                break
            end =text.find('[',start+2)
            out+=text[start+2:end] 
            if(i!=len(s)-1):
                out+=' '
        if(k==1):
            print(out)
        
               

elif(func=='M2T'):
    while(True):
        s =f.readline().strip()
        out=''
        k=1
        copys =s
        if(len(s)==0):
            exit()
        s=s.split()
        for i in range(len(s)):
            start = text.find(']'+s[i]+'[')
            if(start==-1):
                print('Invalid : '+copys)
                k=0
                break
            out+=text[start-1]
        if(k==1):
            print(out)
else:
    print("Invalid code")