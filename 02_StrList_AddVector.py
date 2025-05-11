a =input()
b=input()
first =a.strip("[]").split(",")

second =b.strip("[]").split(",")
third =[0,0,0]

for i in range(3):
    
    first[i] =float(first[i])
    
    second[i]=float(second[i])
    
    third[i]= second[i]+first[i]
  
    
print(str(first)+" + "+str(second)+" = "+str(third) )