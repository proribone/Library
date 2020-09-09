#最大流アルゴリズム(Ford_Fulkerson法)
#グラフをdefaultdictで持つ
#あらかじめ逆辺も追加したグラフを渡す

from collections import defaultdict
import sys
sys.setrecursionlimit(10**7)
 
class Ford_Fulkerson:
    def __init__(self,G,N,s,t):
        self.G,self.N,self.s,self.t=G,N,s,t
        self.max_f=self.Max_Flow(self.G,self.s,self.t)
        
    def dfs(self,G,v,t,f,used):
        if v==t:
            return f
        used[v]=True
        for nv,cap in G[v].items():
            if not used[nv] and cap>0:
                d=self.dfs(self.G,nv,t,min(f,cap),used)
                if d>0:
                    self.G[v][nv]-=d
                    self.G[nv][v]+=d
                    return d
        return 0
 
    def Max_Flow(self,G,s,t):
        flow=0
        while(True):
            used=[False]*self.N
            f=self.dfs(self.G,self.s,self.t,float('inf'),used)
            if f==0:
                return flow
            flow+=f