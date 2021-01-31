'''
最大流(Ford_Fulkerson法)
verified 2021/01/16
http://judge.u-aizu.ac.jp/onlinejudge/review.jsp?rid=5140766#1
https://atcoder.jp/contests/abc010/submissions/19465867
https://atcoder.jp/contests/practice2/submissions/19460982

Ford_Fulkerson(n):
n頂点0辺のグラフを作成

add_edge(u,v,cap):
頂点uから頂点vへ容量cap,流量0の有向辺を追加し、何番目に追加された辺かを返す

Max_Flow(s,t):
頂点sから頂点tへ流せる最大の量を返す


import sys
sys.setrecursionlimit(10**7)
'''

class flow_edge:
    def __init__(self,to,cap,ind):
        self.to,self.cap,self.ind=to,cap,ind
    def items(self):
        return self.to,self.cap,self.ind

class Ford_Fulkerson:
    def __init__(self,N):
        self.G=[[] for _ in range(N)]
        self.N=N
        self.edges=[]

    def add_edge(self,u,v,cap):
        self.edges.append((u,v,cap))
        self.G[u].append(flow_edge(v,cap,len(self.G[v])))
        self.G[v].append(flow_edge(u,0,len(self.G[u])-1))
        return len(self.edges)-1

    def dfs(self,G,v,t,f,used):
        if v==t:
            return f
        used[v]=True
        for i in range(len(G[v])):
            nv,cap,ind=G[v][i].items()
            if not used[nv] and cap>0:
                d=self.dfs(self.G,nv,t,min(f,cap),used)
                if d>0:
                    self.G[v][i].cap-=d
                    self.G[nv][ind].cap+=d
                    return d
        return 0
 
    def Max_Flow(self,s,t):
        flow=0
        while(True):
            used=[False]*self.N
            f=self.dfs(self.G,s,t,float('inf'),used)
            if f==0:
                return flow
            flow+=f