s1=0
s2=0
r=6 
score ={'1':0,'2':0}
point ={'X':0,'R':1,'Y':2,'G':3,'W':4,'B':5,'P':6,'K':7}
while (r!=0):
    k = input()
    if(k[1]=='R'):
        score[k[0]]+= point[k[1]]+point[k[2]]
        r =r-1

k='hh'
while k[1]!='K':
    k = input()
    score[k[0]]+= point[k[1]]

print(str(score['1'])+' '+str(score['2']))
if score['1']>score['2']:
    print("Player 1 wins")
elif score['1']<score['2']:
    print("Player 2 wins")
else:
    print("Tie")

    