n = int(input())
win =[]
lose =[]
for i in range(n):
    w,l = input().split(' ')
    win.append(w)
    lose.append(l)


win = set(win)
lose =set(lose)
lose = list(lose)
for i in lose:
    if(i in win):
        win.remove(i)
    
win=list(win)
print(sorted(win))
