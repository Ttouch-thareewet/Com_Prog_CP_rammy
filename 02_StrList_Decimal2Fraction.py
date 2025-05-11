import math
a=input()
list = a.split(",")

p =int(list[1]+list[2])-int("0"+list[1])

q = int('9'*len(list[2]))* (10**(len(list[1])))
p += int(list[0])*q

k =math.gcd(p,q)
p = p//k
q= q//k
print(p,' / ',q)