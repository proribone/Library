#一点更新区間取得非再帰セグメント木(0-indexed)
#仕様は再帰セグメント木と同じ

import sys
read=sys.stdin.readline

class segtree:
    def __init__(self,n,op,e):
        self.e=e
        self.op=op
        self.size=1<<(n-1).bit_length()
        self.SEG=[self.e]*(self.size*2)
    
    def update(self,i,x):
        i+=self.size
        self.SEG[i]=x
        
        while i>0:
            i>>=1
            self.SEG[i]=self.op(self.SEG[i*2],self.SEG[i*2+1])
    
    def get(self,i):
        return self.SEG[i+self.size]
    
    def query(self,l,r):
        l+=self.size
        r+=self.size
        
        lres,rres=self.e,self.e
        
        while l<r:
            if l&1:
                lres=self.op(lres,self.SEG[l])
                l+=1
            
            if r&1:
                r-=1
                rres=self.op(self.SEG[r],rres)
            
            l>>=1
            r>>=1
            
        res=self.op(lres,rres)
        return res