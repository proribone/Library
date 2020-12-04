'''
verified 2020-12-03
http://judge.u-aizu.ac.jp/onlinejudge/review.jsp?rid=5031396#1
https://atcoder.jp/contests/arc033/submissions/18547688
https://atcoder.jp/contests/practice2/submissions/18547594

0-indexed Binary Indexed Tree

bit(N):長さNの配列Bを作成

add(a,w):B[a]+=w
O(logN)

get(a):B[0]+B[1]+......+B[a-1]
O(logN)

cum(l,r):B[l]+B[l+1]+......+B[r-1]  
O(logN)

lowerbound(w):B[0]+B[1]+....B[i]の和がw以上になるような最小のi
O(logN)
'''

class BIT:
    def __init__(self,N):
        self.N=N
        self.bit=[0]*(N+1)
        self.b=1<<N.bit_length()-1
    def add(self,a,w):
        x=a+1
        while(x<=self.N):
            self.bit[x]+=w
            x+=x&-x
    def get(self,a):
        ret,x=0,a
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
        return x