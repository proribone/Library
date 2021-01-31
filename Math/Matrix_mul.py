def mul(A,B):
    C=[[0]*len(B) for i in range(len(A[0]))]
    for i in range(len(A)):
        for j in range(len(B[0])):
            for k in range(len(B)):
                C[i][j]=(C[i][j]+A[i][k]*B[k][j])
    return C

def matpow(vec,n):
    B=[[0]*len(vec) for i in range(len(vec))]
    for i in range(len(vec)):
        B[i][i]=1
    while(n>0):
        if n&1:
            B=mul(B,vec)
        vec=mul(vec,vec)
        n>>=1
    return B