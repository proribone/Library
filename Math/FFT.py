'''
verified 2020/11/05 https://atcoder.jp/contests/atc001/submissions/17888886
ζを用いた非再帰高速フーリエ変換

convolution(a,b):配列a,bを畳み込んだ配列cを返す
'''

from math import cos,sin,pi
 
def fft(a,n,t,sgn=1):
 
    for i in range(n):
        j=0
        for k in range(t):
            j|=(i>>k&1)<<(t-1-k)
        if i<j:
            a[i],a[j]=a[j],a[i]
    
    b=1
    while(b<n):
        w=1
        zeta=complex(cos((2*pi)/(2*b)),sin((2*pi)/(2*b))*sgn)
        for j in range(b):
            for k in range(0,n,b*2):
                a[j+k],a[j+k+b]=a[j+k]+a[j+k+b]*w,a[j+k]-a[j+k+b]*w
            w*=zeta
        
        b*=2
    if sgn==-1:
        for i in range(n):
            a[i]/=n
    return a
 
def convolution(a,b):
    n=len(a)+len(b)-1
    t=((n-1).bit_length())
    N=1<<t 
    a+=[0]*(N-len(a))
    b+=[0]*(N-len(b))
    
    A=fft(a,N,t)
    B=fft(b,N,t)
    
    for i in range(N):
        A[i]*=B[i]
    
    A=fft(A,N,t,-1)
    for i in range(N):
        A[i]=round(A[i].real)
    return A[:n]