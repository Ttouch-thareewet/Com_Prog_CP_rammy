error =[]
pw =input().strip()
loweralpha='abcdefghijklmnopqrstuvwxyz'
reloweralpha ='zyxwvutsrqponmlkjihgfedcba'
upperalpha='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
numalpha='0123456789'
renumalpha='0987654321'
l1 ='!@#$%^&*()_+'
l2='qwertyuiop'
l3='asdfghjkl'
l4='zxcvbnm'
rel1='+_)(*&^%$#@!)'
rel2='poiuytrewq'
rel3='lkjhgfdsa'
rel4='mnbvcxz'
def no_lowercase(pw):#pw=AAa
    
    for c in pw:
        
        if c in loweralpha:
            return False
            
    return True  
    
def no_uppercase(pw):#pw=AAa
    k=True
    for c in pw:
       
        if c in upperalpha:
            k=False
            
    return k
def no_number(pw):
    for c in pw:
        if  (c<='9'and c>='0'):
            return False
    return True
def no_symbol(pw):
    for c in pw:
        if c not in 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789':
            return False
    return True   
def character_repetition(pw):
    for i in range(len(pw)-3):
        if(pw[i]==pw[i+1] and pw[i]==pw[i+2] and pw[i]==pw[i+3]):
            return True
        
    return False
def number_sequence(pw):
    for i in range(len(pw)-3):
        s = pw[i]+pw[i+1]+pw[i+2]+pw[i+3]
        if(s in numalpha or s in renumalpha):
            return True
    return False
def letter_sequence(pw):
    for i in range(len(pw)-3):
        s = pw[i]+pw[i+1]+pw[i+2]+pw[i+3]
        s = s.lower()
        if(s in loweralpha or s in reloweralpha):
            return True
    return False
def keyboard_pattern(pw):
    for i in range(len(pw)-3):
        s = pw[i]+pw[i+1]+pw[i+2]+pw[i+3]
        s = s.lower()
        if(s in l1 or s in l2 or s in l3 or s in l4):
            return True
        elif(s in rel1 or s in rel2 or s in rel3 or s in rel4):
            return True
    return False
if len(pw)<8:
    error.append('Less than 8 characters')

if no_lowercase(pw):
    error.append('No lowercase letters')
if no_uppercase(pw):
    error.append('No uppercase letters')
if no_number(pw):
    error.append('No numbers')
if no_symbol(pw):
    error.append('No symbols')

if character_repetition(pw):
    error.append('Character repetition')
if number_sequence(pw):
    error.append('Number sequence')
if letter_sequence(pw):
    error.append('Letter sequence')
if keyboard_pattern(pw):
    error.append('Keyboard pattern')
if len(error)==0:
    error.append('OK')

for i in error:
    print(i)