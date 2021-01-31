#getは半開区間
#大文字は64,小文字は96

class RollingHash:
    def __init__(self,S,base,M):
        self.N=len(S)
        self.M=M
        self.H=[0]*(self.N+1)
        self.B=[0]*(self.N+1)
        self.B[0]=1
        for i in range(self.N):
            self.B[i+1]=self.B[i]*base%M
            self.H[i+1]=(self.H[i]*base+(ord(S[i])-64))%M
    def get(self,l,r):
        return (self.H[r]-self.H[l]*self.B[r-l]+self.M)%self.M
    def getall(self,L):
        arr=[]
        for i in range(L,self.N+1):
            arr.append(self.get(i-L,i))
        return arr

def Hash(S,base,M):
    H=0
    for c in S:
        H=(H*base+ord(c)-64)%M
    return H