n = int(input())
lift = []
x = []
c = []
result = []
for i in range (n):
    a = input()
    templist =[]
    templist += a.split()
    for p in range (len(templist)):
        templist[p] = int(templist[p])
    lift.append(templist)
y = int(input())
for i in range (y):
    a = input()
    templist=[]
    templist += a.split()
    for p in range (len(templist)):
        templist[p] = int(templist[p])
    x.append(templist)
for i in range (y):
    for j in range (n):
        if (lift[j][2] - lift[j][1] > 0):
            if (x[i][1] - x[i][0] > 0): 
                if(x[i][0] >= lift[j][1]):
                    if (x[i][1] <= lift[j][2]):
                        c.append(0)
                    else: c.append(x[i][1] - lift[j][2])
                else: c.append((lift[j][2]-x[i][0])+(x[i][1]-x[i][0]))
            else: c.append(abs(lift[j][2]-x[i][0])+(x[i][0]-x[i][1]))
        elif (lift[j][2] - lift[j][1] < 0):
            if(x[i][1] - x[i][0] < 0):
                if(lift[j][1] >= x[i][0]):
                    if(lift[j][2]<=x[i][1]):
                        c.append(0)
                    else: c.append(lift[j][2]-x[i][1])
                else: c.append((x[i][0]-lift[j][2])+(x[i][0]-x[i][1]))
            else: c.append(abs(lift[j][2]-x[i][0])+(x[i][1]-x[i][0]))
        elif (lift[j][2] == lift[j][1]):
            temp = abs(lift[j][2] - x[i][0])
            temp += abs(x[i][0]-x[i][1])
            c.append(temp)
    low = min(c)
    result.append(c.index(low)+1)
    c = []
for i in range (len(result)):
    print(">> ",result[i])

        
         






