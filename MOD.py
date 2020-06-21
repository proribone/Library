MOD=10**9+7

#nCk
def com(n,k,mod):
    res=1
    tmp=1
    for i in range(1,k+1):
        res=res*(n-i+1)%mod
        tmp=tmp*i%mod
    a=pow(tmp,mod-2,mod)
    return res*a%mod

def moddiv(a,m):
    return pow(a,m-2,m)

#逆元テーブル
def facinv(N):
    fac,finv,inv=[0]*(N+1),[0]*(N+1),[0]*(N+1)
    fac[0]=1;fac[1]=1;finv[0]=1;finv[1]=1;inv[1]=1
    for i in range(2,N+1):
        fac[i]=fac[i-1]*i%MOD
        inv[i]=MOD-inv[MOD%i]*(MOD//i)%MOD
        finv[i]=finv[i-1]*inv[i]%MOD
    return fac,finv,inv

#nCr
def COM(n,r):
    if n<r or r<0:
        return 0
    else:
        return ((fac[n]*finv[r])%MOD*finv[n-r])%MOD

#nPr
def PER(n,r):
    if n<r or r<0:
        return 0
    else:
        return (fac[n]*finv[n-r])