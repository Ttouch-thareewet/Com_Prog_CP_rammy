def to_Thai(n):
    out=''
    n =str(n)
    if(int(n)>=1000):
        out += tran[n[0]]+' pun '
        if(n[1]!='0'):
            out += tran[n[1]]+' roi '
        if(n[2]=='2'):
            out+='yi '+'sip '
        elif(n[2]=='1'):
            out+='sip '
        elif(n[2]!='0'):
            out+= tran[n[2]]+' sip '
        if(n[3]=='1'):
            out+='et'
        elif(n[3]!='0'):
            out+=tran[n[3]]
    elif(int(n)>=100):
        out += tran[n[0]]+' roi '
        if(n[1]=='2'):
            out+='yi '+'sip '
        elif(n[1]=='1'):
            out+='sip '
        elif(n[1]!='0'):
            out+= tran[n[1]]+' sip '

        if(n[2]=='1'):
            out+='et'
        elif(n[2]!='0'):
            out+=tran[n[2]]
    elif(int(n)>=10):
        if(n[0]=='2'):
            out+='yi '+'sip '
        elif(n[0]=='1'):
            out+='sip '
        else:
            out+= tran[n[0]]+' sip '
        
        if(n[1]=='1'):
            out+='et'
        elif(n[1]!='0'):
            out+=tran[n[1]]
        
    elif(int(n)>=0):   
        out+=tran[n[0]]
    return out

tran={'0':"soon",'1':"neung",'2':"song",'3':"sam",'4':"si",'5':"ha",'6':"hok",'7':"chet",'8':"paet",'9':"kao"}

exec(input().strip()) 
