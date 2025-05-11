def index_of(grades, ID):
    for i in range(len(grades)):
        if ID ==grades[i][0] :
            return i

    return -1

def upgrade(grades, IDs):
    for i in range(len(IDs)):
        for j in range(len(grades)):
            if(IDs[i]==grades[j][0]):
                if(grades[j][1]=="B+"):
                    grades[j][1]="A"
                elif(grades[j][1]=="B"):
                    grades[j][1]="B+"
                elif(grades[j][1]=="C+"):
                    grades[j][1]="B"
                elif(grades[j][1]=="C"):
                    grades[j][1]="C+"
                elif(grades[j][1]=="D+"):
                    grades[j][1]="C"
                elif(grades[j][1]=="D"):
                    grades[j][1]="D+"
                elif(grades[j][1]=="F"):
                    grades[j][1]="D"
    
    grades.sort()

exec(input())
exec(input())
exec(input())