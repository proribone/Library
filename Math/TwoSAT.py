'''
verified 2020/01/31
https://atcoder.jp/contests/practice2/submissions/19842472
https://judge.yosupo.jp/submission/37298

2-SAT

twosat(n):
n変数の2-SATを作成

add_clause(i,f,j,g):
(x_i=f)∨(x_j=g)というクローズを足す

satisfiable():
条件を満たす割当が存在するならTrue、存在しないならFalseを返す
計算量:クローズの数をmとして O(n+m)

answer():
最後に呼んだsatisfiableの条件を満たす割当を返す
割当が存在しないときの動作は未定義
'''

class twosat:
    
    def __init__(self,n):
        self.G=[[] for _ in range(2*n)]
        self.n=n
    
    def add_clause(self,i,f,j,g):
        self.G[i<<1|(f^1)].append(j<<1|g)
        self.G[j<<1|(g^1)].append(i<<1|f)
    
    def satisfiable(self):
        self.group=self.SCC(self.G,self.n*2)
        for i in range(self.n):
            if self.group[i<<1]==self.group[i<<1|1]:
                return False
        return True
    
    def answer(self):
        ans=[]
        for i in range(self.n):
            if self.group[i<<1]<self.group[i<<1|1]:
                ans.append(True)
            else:
                ans.append(False)
        return ans

    def SCC(self,G,n):
        rG=[[] for _ in range(n)]
        for v in range(n):
            for nv in G[v]:
                rG[nv].append(v)
        
        seen=[0]*n
        order=[]
        for v in range(n):
            if seen[v]:
                continue
            stack=[~v,v]
            while stack:
                v=stack.pop()
                if v>=0:
                    if seen[v]:
                        continue
                    seen[v]=1
                    for nv in G[v]:
                        if not seen[nv]:
                            stack.append(~nv)
                            stack.append(nv)
                else:
                    if seen[~v]==2:
                        continue
                    seen[~v]=2
                    order.append(~v)
        
        C=0
        group=[-1]*n
        for v in order[::-1]:
            if group[v]!=-1:
                continue
            stack=[v]
            while stack:
                v=stack.pop()
                group[v]=C
                for nv in rG[v]:
                    if group[nv]==-1:
                        stack.append(nv)
            C+=1
        
        return group