def palind(m):
    e = len(m) -1
    s = 0
    while(s<e):
        if(m[s]!=m[e]):
            return False
        s+=1
        e-=1
    return True
m = (1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 9, 9, 8, 8, 7, 7, 6, 6, 5, 5, 4, 4, 3, 3, 2, 2, 1, 1)
if (palind(m)):
    print("The Tuple is Filp Flop")
else:
    print("The Tuple is not Filp Flop")