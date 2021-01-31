'''
verified 2020/12/22
https://yukicoder.me/submissions/596580

extgcd(a,b):
ax+by=gcd(a,b)
を解き、gcd(a,b),x,yを返す

crt(B,M):
同じ長さの配列B,Mを渡す
配列の長さをnとしたとき、
x≡B[i] (mod m[i]), ∀i∈{0,1,...,n-1}
を解き、x≡r (mod z) と表せるr,zを返す
答えが存在しないとき(0,1)を返す
n=0のとき(0,1)を返す
extgcdに依存
'''


def extgcd(a,b):
    if b==0:
        return a,1,0
    else:
        r,p=a//b,a%b
        g,x,y=extgcd(b,p)
        return g,y,x-r*y

def crt(B,M):
    r,z=0,1
    for b,m in zip(B,M):
        b1,m1=r,z
        b2,m2=b,m
        g,x,y=extgcd(m1,m2)
        x,y=(b2-b1)//g*x,(b2-b1)//g*y
        if b1%g!=b2%g:
            return (0,0)
        a=(m1*x+b1)%(m1*m2//g)
        r,z=a,m1*m2//g
    return r,z