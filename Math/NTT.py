'''
verified 2020/11/05 https://atcoder.jp/contests/practice2/submissions/17893800
非再帰数論変換(NTT)
原始根があるNTT-friendlyなMODで使用可能

MOD:NTT-friendlyなMODの値
g:MODの原始根
convolution(a,b):配列a,bをMODで畳み込んだ配列cを返す
'''

MOD=998244353
g=3
roots=[pow(g,(MOD-1)>>i,MOD) for i in range(24)]
inv_roots=[pow(r,MOD-2,MOD) for r in roots]
 
def ntt(a,n,t,sgn=1):
    ninv=pow(n,MOD-2,MOD)
 
    for i in range(n):
        j=0
        for k in range(t):
            j|=(i>>k&1)<<(t-1-k)
        if i<j:
            a[i],a[j]=a[j],a[i]
    
    b=1
    for i in range(t):
        
        w=1
        omega=roots[(2*b-1).bit_length()] if sgn==1 else inv_roots[(2*b-1).bit_length()]
        
        for j in range(b):
            for k in range(0,n,b*2):
                a[j+k],a[j+k+b]=(a[j+k]+a[j+k+b]*w)%MOD,(a[j+k]-a[j+k+b]*w)%MOD
            w=w*omega%MOD

        b*=2
    if not sgn:
        for i in range(n):
            a[i]=a[i]*ninv%MOD
 
def convolution(a,b):
    n=len(a)+len(b)-1
    t=((n-1).bit_length())
    N=1<<t
    a+=[0]*(N-len(a))
    b+=[0]*(N-len(b))
    
    ntt(a,N,t)
    ntt(b,N,t)
    
    for i in range(N):
        a[i]=a[i]*b[i]%MOD
    
    ntt(a,N,t,0)
    return a[:n]