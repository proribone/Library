#有向グラフを強連結分解し、処理後のグラフのサイズ・各頂点のグループを返す
#setでグラフを構築してトポロジカルソートすると良い

def SCC(G,N,M):
    rG=[[] for _ in range(N)]
    P=[]
    seen=[0]*N
    for v in range(N):
        for nv in G[v]:
            rG[nv].append(v)
            
    def dfs(G,v):
        seen[v]=1
        for nv in G[v]:
            if not seen[nv]:
                dfs(G,nv)
        P.append(v)
    
    def rdfs(G,v,C):
        seen[v]=1
        group[v]=C
        for nv in G[v]:
            if not seen[nv]:
                rdfs(G,nv,C)
    for v in range(N):
        if not seen[v]:
            dfs(G,v)
    
    seen=[0]*N
    group=[-1]*N
    C=0
    for v in P[::-1]:
        if not seen[v]:
            rdfs(rG,v,C)
            C+=1
            
    Size=max(group)+1
    return group,Size