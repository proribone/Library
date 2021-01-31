'''
(使用非推奨)
0-indexed 抽象化再帰セグメント木

SEGTree(n,op,e):
長さnの配列Sを作成
eを単位元とする演算opによる区間取得が可能

update(i,x):
S[i]をxで更新 O(logN)

get(a,b):
op(S[a],S[a+1],.....S[b-1])を計算 O(logN)
'''

class SEGTree:
    def __init__(self,n,op,e):
        self.Unit=e
        self.Op=op
        i=1<<(n.bit_length()-1)
        if i!=n:
            i*=2
        self.SEG=[self.Unit]*(2*i-1)
        self.d=i
    def update(self,i,x):
        i+=self.d-1
        self.SEG[i]=x
        while i>0:
            i=(i-1)//2
            self.SEG[i]=self.Op(self.SEG[i*2+1],self.SEG[i*2+2])
    def find(self,a,b,k,l,r):
        if r<=a or b<=l:
            return self.Unit
        if a<=l and r<=b:
            return self.SEG[k]
        else:
            c1=self.find(a,b,2*k+1,l,(l+r)//2)
            c2=self.find(a,b,2*k+2,(l+r)//2,r)
            return self.Op(c1,c2)
    def get(self,a,b):
        return self.find(a,b,0,0,self.d)
