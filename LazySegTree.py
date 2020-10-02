'''

verified 2020/10/02 
https://atcoder.jp/contests/practice2/submissions/17138406
https://atcoder.jp/contests/abl/submissions/17138370
https://atcoder.jp/contests/abc179/submissions/17138337

抽象化非再帰遅延評価セグメント木

n:
配列サイズ

op:
区間取得演算

e:
opの単位元

mapping:
区間作用の値への反映
mapping(f,x)で渡す

Id:
作用・マージで変化を及ぼさないような恒等写像

composition:
2つの変更のマージ
composition(new,old)で渡す

arr:
初期配列

update(l,r,x):
半開区間[l,r)にxを作用

query(l,r):
半開区間[l,r)の値を取得

get(i):
i番目の値を取得

※
data・lazyがtupleになる場合はoffsetで整数にする
入力はsys.stdin.readline
Idがmapping, compositionの両方で変化を与えないように注意

'''

class lazysegtree:
    def __init__(self,n,op,e,mapping,Id,composition,arr=[]):
        self.log=(n-1).bit_length()
        self.size=1<<self.log
        self.op=op
        self.e=e
        self.mapping=mapping
        self.Id=Id
        self.composition=composition
        self.data=[self.e]*(self.size*2)
        self.lazy=[self.Id]*(self.size*2)
        
        if arr:
            for i in range(n):
                self.data[i+self.size]=arr[i]
            for i in reversed(range(self.size)):
                self.data[i]=self.op(self.data[i<<1],self.data[i<<1|1])
 
    
    def update(self,l,r,x):
        if l>=r:
            return self.e
        l+=self.size
        r+=self.size
        l0,r0=l//(l&-l),r//(r&-r)-1
        self.propagate_above(l0)
        self.propagate_above(r0)
        
        while l<r:
            if l&1:
                self.lazy[l]=self.composition(x,self.lazy[l])
                l+=1
            
            if r&1:
                r-=1
                self.lazy[r]=self.composition(x,self.lazy[r])
            
            l>>=1
            r>>=1
 
        self.calc_above(l0)
        self.calc_above(r0)
 
    def query(self,l,r):
        if l>=r:
            return
        
        l+=self.size
        r+=self.size
        l0,r0=l//(l&-l),r//(r&-r)-1
        self.propagate_above(l0)
        self.propagate_above(r0)
        
        lres,rres=self.e,self.e
        while l<r:
            if l&1:
                lres=self.op(lres,self.calc(l))
                l+=1
            if r&1:
                r-=1
                rres=self.op(self.calc(r),rres)
            l>>=1
            r>>=1
        return self.op(lres,rres)
 
    def get(self,i):
        i+=self.size
        self.propagate_above(i)
        return self.calc(i)
 
    def propagate(self,i):
        v=self.lazy[i]
        self.data[i]=self.calc(i)
        self.lazy[i<<1]=self.composition(v,self.lazy[i<<1])
        self.lazy[i<<1|1]=self.composition(v,self.lazy[i<<1|1])
        self.lazy[i]=self.Id
    
    def propagate_above(self,i):
        H=i.bit_length()
        for h in range(H,0,-1):
            self.propagate(i>>h)
    
    def calc(self,i):
        return self.mapping(self.lazy[i],self.data[i])
    
    def calc_above(self,i):
        i>>=1
        while i:
            self.data[i]=self.op(self.calc(i<<1),self.calc(i<<1|1))
            i>>=1