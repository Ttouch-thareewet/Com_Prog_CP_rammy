a=input()
num1=0
num2=0
x1=4
x2=4
for i in range(32):
    if(i%7==3):
        num1+= int(a[i])* pow(10,x1)
        x1=x1-1
    if(i%5==2 and i!=2):
        num2+= int(a[i])* pow(10,x2)
        x2=x2-1

num3=num1+num2+10000
num3 =num3%10000
r =num3%10
num3 = (num3-r)/10 #813



n1 = num3//100 + ((num3%100)-num3%10)/10 +num3%10#12
n2 =   n1%10+1
out = str(int(num3))
if(num3<=99 and num3>=10 ):
    out="0"+str(int(num3))

if(num3<=9):
    out="00"+str(int(num3))
code = ""

if(n2 == 1):
    code = "A"
elif(n2 == 2):
    code = "B"
elif(n2 == 3):
    code = "C"
elif(n2 == 4):
    code = "D"
elif(n2 == 5):
    code = "E"
elif(n2 == 6):
    code = "F"
elif(n2 == 7):
    code = "G"
elif(n2 == 8):
    code = "H"
elif(n2 == 9):
    code = "I"
elif(n2 == 10):
    code = "J"

print(out + code)
