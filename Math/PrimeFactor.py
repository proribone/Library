#素数判定
def is_prime(n):
    t=True
    for i in range(2,int(n**0.5)+1):
        if(n%i)==0:
            t=False
            break
    return t

#素数列挙
def primes(n):
    if n==1 or n==0:
        return []
    arr=[True]*(n+1)
    arr[0],arr[1]=False,False
    p=[]
    for i in range(2,n+1):
        if arr[i]==False:
            continue
        p.append(i)
        for j in range(i*2,n+1,i):
            arr[j]=False
    return p

#約数列挙
def factor(N):
    arr=[]
    for i in range(1,int(N**0.5)+1):
        if(N%i==0):
            arr.append(i)
            if(N//i!=i):
                arr.append(N//i)
    return arr

#素因数分解
def factorization(n):
    arr=[]
    tmp=n
    for i in range(2,int(n**0.5)+1):
        if(tmp%i==0):
            cnt=0
            while tmp%i==0:
                cnt+=1
                tmp//=i
            arr.append([i,cnt])
    if(tmp!=1):
        arr.append([tmp,1])
    return arr

#n進数での桁数判定(n=数値、k=進数)
def keta(n,k):
    cnt=0
    while(n!=0):
        n//=k
        cnt+=1
    return cnt
