n = int(input())
l=[]
actor={}
for i in range(n):
    s =input().split(', ')
    for j in range(1,len(s)):
        movie = s[0]
        if(s[j] in actor):
            actor[s[j]].append(movie)
        else:
            actor[s[j]] = [movie]
            
out =input().split(', ')
for i in range(len(out)):
    if(out[i] in actor):
        print(out[i]+ '  -> '+ ', '.join(actor[out[i]]))
    else:
        print(out[i]+ '  -> '+ 'Not found')