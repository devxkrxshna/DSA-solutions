def decodeMessage(key,message):
    hasht={" ":" "}
    j=97
    new_message=[]
    for k in key:
        if k not in hasht and k!=" ":
            hasht[k]=chr(j)
            j+=1
    for m in message:
            new_message.append(hasht[m])
    return "".join(new_message)
    

print(decodeMessage("the quick brown fox jumps over the lazy dog","vkbs bs t suepuv"))