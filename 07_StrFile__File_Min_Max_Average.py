a,year =input().strip().split()
f =open(a,'r')
fr =f.readline()

k=0

sum =0
while len(fr)!=0:
    if(fr[0]==year[2] and fr[1]==year[3]):
        k+=1
        score =float(fr.split()[1])
        if(k==1):
            min =score
            max =score
        if(score>max):
            max=score
        if(min>score):
            min = score
        sum+=score

    fr =f.readline()
if(k==0):
    print("No data")
else:
    avg = sum/k
    print(min,max,avg)
f.close()