#1-indexed
#addはaにwを加算する
#get,cumは半開区間

class BIT:
    def __init__(self,N):
        self.N=N
        self.bit=[0]*(N+1)
        self.b=1<<N.bit_length()-1
    def add(self,a,w):
        x=a
        while(x<=self.N):
            self.bit[x]+=w
            x+=x&-x
    def get(self,a):
        ret,x=0,a-1
        while(x>0):
            ret+=self.bit[x]
            x-=x&-x
        return ret
    def cum(self,l,r):
        return self.get(r)-self.get(l) 
    def lowerbound(self,w):
        if w<=0:
            return 0
        x=0
        k=self.b
        while k>0:
            if x+k<=self.N and self.bit[x+k]<w:
                w-=self.bit[x+k]
                x+=k
            k//=2
        return x+1
