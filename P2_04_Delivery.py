out =[]

while(True):
    g = input()
    
    if(g=='END'):
        break
    
    number,func,day,month,year = g.split()
    
    if(int(year)<2558):
        print("Error: "+g+" --> Invalid year")
        continue
    if not(1<=int(month)<=12):
        print("Error: "+g+" --> Invalid month")
        continue
    if  month=='2' and not(1<=int(day)<=29):
        print("Error: "+g+" --> Invalid date")
        continue
    if(day=='29' and month=='2' ):
        cyear = int(year)-543
        if not(cyear%400==0 or (cyear%4==0 and cyear%100!=0)):
              print("Error: "+g+" --> Invalid date")
              continue
        
    if not(1<=int(day)<=31):
        print("Error: "+g+" --> Invalid date")
        continue
    if  (month in '469' or month=='11') and (int(day)<1 or int(day)>30):
        print("Error: "+g+" --> Invalid date")
        continue

    
    
    if(func not in'EQNF' or len(func)!=1):
        print("Error: "+g+" -->  Invalid delivery type")
        continue
    
    t ={'E':1,'Q':3,'N':7,'F':14}
    d=int(day)+t[func]
    m=int(month)
    y=int(year)
    if(month=='12'):
        if d>31:
            d=d%31
            m=1
            y+=1
    elif month=='2':
        cyear = int(year)-543
        if (cyear%400==0 or (cyear%4==0 and cyear%100!=0)):#29
            if(d>29):
                d=d%29
                m+=1
        else:
            if(d>28):
                d=d%28
                m+=1
    elif month in '469' or month=='11':
        if(d>30):
            d=d%30
            m+=1
    else :
        if d>31:
           d=d%31
           m+=1

    year=str(y)
    day =str(d)
    month=str(m)
    if(int(month)<10):
        if(int(day)<10):
            out.append([year+'/'+'0'+month+'/'+'0'+day,number])
        else:
            out.append([year+'/'+'0'+month+'/'+day,number])
    else:
        if(int(day)<10):
            out.append([year+'/'+month+'/'+'0'+day,number])
        else:
            out.append([year+'/'+month+'/'+day,number])
     
out =sorted(out)  

if(len(out)!=0):
    for i in range(len(out)):
        print(out[i][1]+ ':'+ ' delivered on ' ,end='')
    
        k=''
        y,m,d=out[i][0].split("/")
        if(m[0]=='0'):
            if(d[0]=='0'):
            
                k=d[1]+'/'+m[1]+'/'+y
            else:
                k=d +'/'+m[1]+'/'  +y 
        else:
            if(d[0]=='0'):
                k=d[1]+'/'+m+'/'+y
            else:
                k=d+'/'+m+'/'+y
        print(k)
