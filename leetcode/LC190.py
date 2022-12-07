def reverseBits(n):
    rev_n=n[::-1]
    dec_value=0
    for i,pow in enumerate(reversed(range(len(rev_n)))):
        dec_value+=int(rev_n[i])*(2**pow)
    return dec_value
a=reverseBits("00000010100101000001111010011100")
print(a)
        