def lengthOfLastWord(s):
    return len(s.rstrip()[::-1].split()[0])


a=lengthOfLastWord("hello gh")
print(a)
    
    