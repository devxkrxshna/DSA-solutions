
def smallestDifference(arrone,arrtwo):
    arrone.sort()
    arrtwo.sort()
    idx1=0
    idx2=0
    currentsmallest=float('inf')
    smallest=float('inf')
    while idx1<len(arrone) and idx2<len(arrtwo):
        firstnum=arrone[idx1]
        secondnum=arrtwo[idx2]
        if firstnum<secondnum:
            currentsmallest=secondnum-firstnum
            idx1+=1
        elif secondnum<firstnum:
            currentsmallest=firstnum-secondnum
            idx2+=1
        else:
            return [firstnum,secondnum]
        if currentsmallest<smallest:
            smallest=currentsmallest
            smallestpair=[firstnum,secondnum]
    return smallestpair


a=smallestDifference([-1,5,10,20,28,3],[26,134,135,15,17])
print(a)
            
            
        
        