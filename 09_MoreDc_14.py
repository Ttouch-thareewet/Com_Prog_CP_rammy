course = input().strip()
teacher = input().strip()
database = input().strip()
fteacher = open(teacher,'r')
fcourse = open(course,'r')
fdatabase = open(database,'r')
matching =[]
while (True):
    s= fdatabase.readline().strip()
    if(len(s)==0):
        break
    a,b =s.split(',')#course,teacher
    matching.append([int(a),int(b)])
    
cou ={}#course dict
tea ={}#teacher dict
while (True):
    s=fteacher.readline().strip()
    if(len(s)==0):
        break
    a,b = s.split(',')
    tea[int(a)]=b
    
while (True):
    s=fcourse.readline().strip()
    if(len(s)==0):
        break
    a,b = s.split(',')
    cou[int(a)]=b
out=[]
for i in range(len(matching)):
    if(matching[i][0] in cou and matching[i][1] in tea):
        
        out.append(cou[matching[i][0]]+','+tea[matching[i][1]])
    else:
        out.append('record error')

    
for i in out :
    print(i)
    
fteacher.close()
fcourse.close()
fdatabase.close()   
