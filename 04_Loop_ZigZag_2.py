k = input()
a,b= k.split()
a= int(a)
b= int(b)
minzig=a
maxzig=b
minzag=b
maxzag=a
k=1
i =1
def checkmaxzig(n,maxzig):
    if(n>maxzig):
        maxzig=n
    return maxzig
def checkminzig(n,minzig):
    if(n<minzig):
        minzig=n 
    return minzig
def checkmaxzag(n,maxzag):
    if(n>maxzag):
        maxzag=n
    return maxzag
def checkminzag(n,minzag):
    if(n<minzag):
        minzag=n 
    return minzag
while k==1:
    c=input()
    if(c=="Zig-Zag"):
        print(str(minzig)+" "+str(maxzig))
        break
    if(c=="Zag-Zig"):
        print(str(minzag)+" "+str(maxzag))
        break
    a,b =c.split()
    a=int(a)
    b=int(b)
    if(i%2==1):
        maxzig =checkmaxzig(a,maxzig)
        minzag =checkminzag(a,minzag)
        maxzag =checkmaxzag(b,maxzag)
        minzig =checkminzig(b,minzig)
    else :
        minzig =checkminzig(a,minzig)
        maxzag =checkmaxzag(a,maxzag)
        maxzig =checkmaxzig(b,maxzig)
        minzag =checkminzag(b,minzag)
    i = i+1