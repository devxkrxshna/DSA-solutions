def validateSubsequence(arr,seq):
    arr_i=0
    seq_i=0
    while arr_i<len(arr) and seq_i<len(seq):
        if seq_i==len(seq):return True
        if arr[arr_i]==seq[seq_i]:
            seq_i+=1
        arr_i+=1
    return seq_i==len(seq)

a=validateSubsequence([5,1,122,25,6,-1,8,10],[1,6,-1,10])
print(a)