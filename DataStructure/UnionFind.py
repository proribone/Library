'''
Union-Find Tree
0-indexed

各操作の計算量はたぶんO(α(N))

UnionFind(N):
N頂点0辺で初期化

union(a,b):
辺(a,b)を追加 もともと連結だった場合何もしない

size(a):
頂点aが属する連結成分のサイズ

same(a,b):
aとbが属する連結成分が等しいときTrue, 異なるときFalse
'''

class UnionFind:
    def __init__(self,N):
        self.par=[i for i in range(N)]
        self.siz=[1 for _ in range(N)]
        self.rank=[0 for _ in range(N)]
    def find(self,x):
        if self.par[x]==x:
            return x
        else:
            self.par[x]=self.find(self.par[x])
            return self.par[x]
    def union(self,a,b):
        a=self.find(a)
        b=self.find(b)
        if a==b:
            return 0
        else:
            if self.rank[a]>self.rank[b]:
                self.par[b]=a
                self.siz[a]+=self.siz[b]
            else:
                self.par[a]=b
                self.siz[b]+=self.siz[a]
                if self.rank[a]==self.rank[b]:
                    self.rank[b]+=1
    def size(self,a):
        return self.siz[self.find(a)]
    def same(self,a,b):
        return self.find(a)==self.find(b)