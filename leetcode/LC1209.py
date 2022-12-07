def removeDuplicates(s, k):
    stack=[["#",0]] #initialising our stack
    for c in s: #for each character in the given string
        if stack[-1][0]==c: #if the character at the top of string equal to the character in s
            stack[-1][1]+=1 #update the count
            if stack[-1][1]==k: #if count== given k
                stack.pop() #pop the list from the top of the stack
        else:
            stack.append([c,1]) #if top chara in stack is not equal to c, push the character with count 1
    return ''.join(c*k for c,k in stack) #join the string by expanding (0 multiplied by anthing is nothing so we are safe)

a=removeDuplicates("deeedbbcccbdaa",3)
print(a)
           

            