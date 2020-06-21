#ダイクストラ法

from heapq import heappush,heappop,heapify
INF=10**30

def dijkstra(G,s,n):
    que=[(0,s)]
    dist=[INF]*n
    dist[s]=0
    while que:
        mincost,u=heappop(que)
        if(mincost>dist[u]):
            continue
        for c,v in G[u]:
            if(dist[u]+c<dist[v]):
                dist[v]=dist[u]+c
                heappush(que,(dist[v],v))
    return dist