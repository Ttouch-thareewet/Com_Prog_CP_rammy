month =["January",
"February",
'March',
'April',
'May',
'June',
'July',
'August',
'September',
'October',
'November',
'December']

name1,month1,day1,year1 =input().split()
name2,month2,day2,year2 =input().split()
nday1=0
nday2=0
month1=month.index(month1)
month2=month.index(month2)
if(len(day1)==3):
    nday1=int(day1[0]+day1[1])
else:
    nday1=int(day1[0])

if(len(day2)==3):
    nday2=int(day2[0]+day2[1])
else:
    nday2=int(day2[0])
if(year1>year2):
    print(name2)
elif(year2>year1):
    print(name1)
else:
    if(month1>month2):
        print(name2)
    elif(month1<month2):
        print(name1)
    else:
        if(nday1>nday2):
            print(name2)
        elif(nday1<nday2):
            print(name1)
        else :
            print(name1+" "+name2)


