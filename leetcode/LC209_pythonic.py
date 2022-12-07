def minSubArrayLen( s, A):
        i, res = 0, len(A) + 1
        for j in range(len(A)):
            s -= A[j]
            while s <= 0:
                res = min(res, j - i + 1)
                s += A[i]
                i += 1
        return res % (len(A) + 1)
a=minSubArrayLen(7,[2,3,1,2,4,3])
print(a)