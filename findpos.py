list1 = list(range(1,100))
def findpos(l,v):
    for x in l:
        if x == v:
            return(l.index(x))
    else:
        return(-1)
    
