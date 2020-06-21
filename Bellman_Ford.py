INF=10**30
#閉路検出
def Belman_Ford(s,N,Edge):
    dist=[INF]*N
    dist[s]=0
    cnt=0
    neg=False
    while True:
        update=False
        for f,t,c in Edge:
            if dist[t]>dist[f]+c:
                if cnt<N-1:
                    if dist[f]!=INF:
                        dist[t]=min(dist[t],dist[f]+c)
                        update=True
                else:
                    neg=True
        if not update:
            break
        cnt+=1
    if neg:
        return -1
    else:
        return dist
#全閉路検出
def Belman_Ford_2(s,N,Edge):
    dist=[INF]*N
    neg=[False]*N
    dist[s]=0
    for _ in range(N-1):
        for f,t,c in Edge:
            if dist[t]>dist[f]+c and dist[f]!=INF:
                dist[t]=min(dist[t],dist[f]+c)
    for _ in range(N):
        for f,t,c in Edge:
            if dist[t]>dist[f]+c and dist[f]!=INF:
                dist[t]=dist[f]+c
                neg[t]=True
            if neg[f]:
                neg[t]=True
    return dist,neg