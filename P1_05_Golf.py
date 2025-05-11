sumpar=0
sumstroke=0
sumstrokechange=0
handicap =0
for i in range (9):
    par,stroke,choose=(input().split())
    par =int(par)
    stroke = int(stroke)
    choose = int(choose)
    sumpar+=par
    sumstroke+=stroke
    if(choose==1):
        sumstrokechange +=min(par+2,stroke)

handicap = int((0.8*(1.5*sumstrokechange-sumpar))//1)
total =sumstroke-handicap
print(sumstroke)
print(handicap)
print(total)