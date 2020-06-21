#最小共通祖先

import sys
sys.setrecursionlimit(10**7)

class LCA:
    def __init__(self,N,G,r):
        self.dist=[-1]*N
        self.K=0
        while(2**self.K<N):
            self.K+=1
        self.doubling=[[-1]*N for i in range(self.K+1)]
        self.dfs(G,r,-1,0)
        for k in range(1,self.K+1):
            for i in range(1,N):
                self.doubling[k][i]=self.doubling[k-1][self.doubling[k-1][i]]
        
    def dfs(self,G,v,p,d):
        self.dist[v]=d
        self.doubling[0][v]=p
        for nv in G[v]:
            if nv==p:
                continue
            self.dfs(G,nv,v,d+1)
        
    def get(self,u,v):
        if self.dist[u]<self.dist[v]:
            u,v=v,u
        for k in range(self.K+1):
            if (self.dist[u]-self.dist[v])>>k&1:
                u=self.doubling[k][u]
        if u==v:
            return u
        for k in reversed(range(self.K+1)):
            if self.doubling[k][u]!=self.doubling[k][v]:
                u=self.doubling[k][u]
                v=self.doubling[k][v]
        return self.doubling[0][u]
    
    def getdist(self,u,v):
        return self.dist[u]+self.dist[v]-2*self.dist[self.get(u,v)]