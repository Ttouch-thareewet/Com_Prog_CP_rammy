def spiral_square(n): # n is a positive odd number
    s=[]
    for i in range(n):
        a=[]
        for j in range(n):
            a.append(0)
        s.append(a)
            
    x=n-1
    y=n-1
    k=1   #1 goleft 2go up 3go right 4 go down
    for i in range(n*n):
        number=n*n-i
        if(k%4==1):
            s[y][x] = number
            if(x-1<0 or s[y][x-1]!=0):
                k+=1
                y-=1
            else:
               x-=1 
        elif(k%4==2):
            s[y][x]=number
            if(y-1<0 or s[y-1][x]!=0):
                k+=1
                x+=1
            else:
                y-=1
        elif(k%4==3):
            s[y][x]=number
            if(x+1>n-1 or s[y][x+1]!=0):
                k+=1
                y+=1
            else:
                x+=1
        elif(k%4==0):
            s[y][x]=number
            if( y+1>n-1 or s[y+1][x]!=0):
                k+=1
                x-=1
            else:
                y+=1
        
    return s
        
    
def print_square(S):
 # เรยีกใชฟ้ ังกช์ นั นเี้พอื่ แสดงคา่ ของ S ที่เป็นลิสต์ของลิสต์ของจ านวนเต็ม
    for i in range(len(S)):
        print(' '.join([(2*' '+str(e))[-3:] for e in S[i]]))
        
exec(input().strip())

