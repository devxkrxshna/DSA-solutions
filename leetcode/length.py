# Function to find permutations of a given string


 
def allPermutations(digit):
    from itertools import permutations
    perm_list=[]
      
     # Get all permutations of string 'ABC'
    permList = permutations(digit)
 
     # print all permutations
    for perm in list(permList):
        perm_list.append(''.join(perm))
    for i in range(len(digit)):
        for j in range(0,len(digit)-1):
            perm_list.append(''.join([digit[i],digit[j]]))
    return perm_list


def length(digit,passwords):
    count=0
    
    
    perm_list=allPermutations(digit)
    
    for i in passwords:
        for j in perm_list:
            if i==j:
                count+=1
    return count


    
            
            
    
       
