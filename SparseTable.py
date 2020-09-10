#opで演算、eで単位元を指定
#getは半開区間

class SparseTable:
    def __init__(self,arr,N,op,e):
        self.A=arr
        self.N=N
        self.Unit=e
        self.Op=op
        self.K=N.bit_length()-1
        self.pow2=[1]
        for i in range(self.K):
            self.pow2.append(self.pow2[-1]*2)
        self.ST=[[self.Unit]*(self.K+1) for i in range(N)]
        for i in range(N):
            self.ST[i][0]=self.A[i]
        for i in reversed(range(N)):
            for k in range(1,self.K+1):
                if self.N<i+self.pow2[k]:
                    break
                self.ST[i][k]=self.Op(self.ST[i][k-1],self.ST[i+self.pow2[k-1]][k-1])
    def get(self,l,r):
        if l==r:
            return self.Unit
        x=r-l
        t=x.bit_length()-1
        return self.Op(self.ST[l][t],self.ST[r-self.pow2[t]][t])