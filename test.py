# f =open('data.txt','r')
# l1 = f.readline().strip()
# l2 =f.readline().strip()
# print(l1)
# print(l2)
# print("aaa"+'\n'+"ss")
# a = {'a':1,"c":3,"b":2}
# k= sorted(a)
# c =sorted(a.items())
# print(k)
# print(c)
# print(a.items())
# l =[1.00,0.5,6.0]
# a= sorted(l)
# print(a)
# print([1,2]+[2,3])
# c="1,2,3,4"
# k =set(c.split(','))
# print(k)
# 
# l= ['1','2','3','4']
# c= l+l[-1::-1]
# print(c)
# try :
#     print(int('A0'))
# except:
#     print(int('99'))
# a ='fakakf'
# print(a[1:5])
# for i in range(10):
#     print(i)
#     i+=3
n=3
s=[]
for i in range (n):
    a=[]
    for j in range (n):
        a.append(0)
    s.append(a)
print(s)
x=n-1
y=n-1
k=1   #1 goleft 2go up 3go right 4 go down
for i in range(n*n):
    number=n*n-i
    if(k%4==1):
        s[x][y] = number
        if(x-1<0 or s[x-1][y]!=0):
            y-=1
            k+=1
        else:
            x-=1
    elif(k%4==2):
        s[x][y]=number
        if(y-1<0 or s[x][y-1]!=0):
            k+=1
            x+=1
        else:
            y-=1
    elif(k%4==3):
        s[x][y]=number
        if(x+1>n-1 or s[x+1][y]!=0):
            k+=1
            y+=1
        else:
            x+=1
    elif(k%4==0):
        s[x][y]=number
        if( y+1>n-1 or s[x][y+1]!=0):
            k+=1
            x-=1
        else:
            y+=1
def print_square(S):
 # เรยีกใชฟ้ ังกช์ นั นเี้พอื่ แสดงคา่ ของ S ที่เป็นลิสต์ของลิสต์ของจ านวนเต็ม
    for i in range(len(S)):
        print(' '.join([(2*' '+str(e))[-3:] for e in S[i]]))
print_square(s)
print(s[0][1])          
print(s)