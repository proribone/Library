#0-indexed
#cum,bitは半開区間

class BIT:
    def __init__(self,N):
        self.N=N
        self.bit=[0]*N
    def add(self,a,w):
        x=a
        while(x<self.N):
            self.bit[x]+=w
            x|=x+1
    def get(self,a):
        ret,x=0,a-1
        while(x>=0):
            ret+=self.bit[x]
            x=(x&(x+1))-1
        return ret
    def cum(self,l,r):
        return self.get(r)-self.get(l) 