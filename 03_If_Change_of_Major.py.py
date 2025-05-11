out1 =input()
out2 =input()

num1,g1,gcom1,g1cal1,g1cal2=out1.split()
num2,g2,gcom2,g2cal1,g2cal2=out2.split()
ac1 = False
ac2 = False

if(gcom1=='A' and g1cal1<='C' and g1cal2<='C'  ):
    ac1 =True

if(gcom2=='A' and g2cal1<='C' and g2cal2<='C'  ):
    ac2 =True


if(ac1==False and ac2==False):
    print("None")
elif(ac1==True and ac2==False):
    print(num1)
elif(ac1==False and ac2==True):
    print(num2)  
else :
    if(g1>g2):
        print(num1)
    elif (g1<g2):
        print(num2)
    else :
        if(g1cal1<g2cal1):
            print(num1)
        elif (g1cal1>g2cal1):
            print(num2)
        else :
            if(g1cal2<g2cal2):
                print(num1)
            elif (g1cal2>g2cal2):
                print(num2)
            else :
                print("Both")


    



