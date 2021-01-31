'''
幅優先探索(BFS)

bfs(G,s,N):
頂点数Nの重みなしグラフGにおけるsを始点とした各頂点への最小コスト
dist[v]=頂点vへの最小コスト
'''
from collections import deque
def bfs(G,s,N):
    dist=[-1]*N
    d=deque()
    dist[s]=0
    d.append(s)
    while(len(d)!=0):
        v=d[0]
        d.popleft()
        for nv in G[v]:
            if(dist[nv]!=-1):
                continue
            dist[nv]=dist[v]+1
            d.append(nv)
    return dist

'''
グリッド上の幅優先探索

mbfs(G,sh,sw,H,W):
H行W列のグリッドGにおける(sh,sw)を始点とした各頂点への最小コスト
dist[h][w]=(h,w)への最小コスト
'''
from collections import deque
def mbfs(G,sh,sw,H,W):
    dist=[[-1]*W for i in range(H)]
    dist[sh][sw]=0

    d=deque()
    d.append([sh,sw])
    dx=[1,0,-1,0]
    dy=[0,1,0,-1]
    while(len(d)!=0):
        h=d[0][0]
        w=d[0][1]
        d.popleft()
        for dir in range(4):
            nh=h+dx[dir]
            nw=w+dy[dir]
            if(nh>H-1 or nh<0 or nw>W-1 or nw<0):
                continue
            if(dist[nh][nw]!=-1 or G[nh][nw]=='#'):
                continue
            dist[nh][nw]=dist[h][w]+1
            d.append([nh,nw])
    return dist
