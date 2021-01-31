'''
ダイクストラ法

dijkstra(G,s,n):
n頂点の重み付きグラフGにおけるsを始点とした各頂点への最小コスト
dist[v]=頂点vまでの最小コスト
'''

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

'''
グリッド上のダイクストラ法
座標(x,y)をintに圧縮している

dijkstra(G,H,W,sh,sw,cost):
H行W列のグリッドGにおける(sh,sw)を始点とした各頂点への最小コスト
各辺の重みがcostで指定されている
dist[h][w]=(h,w)までの最小コスト
'''

INF=10**30
from heapq import heappop,heappush,heapify
def dijkstra(G,H,W,sh,sw,cost):
    dx=[1,0,-1,0]
    dy=[0,1,0,-1]
    que=[(0,sh*10000+sw)]
    dist=[[INF]*W for i in range(H)]
    dist[sh][sw]=0
    while que:
        mincost,u=heappop(que)
        h,w=u//10000,u%10000
        if(mincost>dist[h][w]):
            continue
        for di in range(4):
            nh=h+dx[di]
            nw=w+dy[di]
            if(nh>H-1 or nh<0 or nw>W-1 or nw<0):
                continue
            if(G[nh][nw]=='#'):
                continue
            if(dist[h][w]+cost<dist[nh][nw]):
                dist[nh][nw]=dist[h][w]+cost
                heappush(que,(dist[nh][nw],nh*10000+nw))
    return dist
