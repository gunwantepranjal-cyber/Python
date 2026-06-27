L = [ 10,20,0,-23,-1,0,34]
for x in L:
    if x < 0:
        cube = x * x * x
    elif x == 0:
        print(x)
    else:
        sq = x * x
        print(sq)
    
