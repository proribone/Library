'''
トポロジカルソート

tsort(In,G):
グラフGのトポロジカルソート
In[v]=頂点vの入次数

コメント部分を有効にすると、トポロジカルソートが構築出来なかったときに-1を出力して終了する
'''

from collections import deque
def tsort(In,G):
    que=deque([i for i,c in enumerate(In) if c==0])
    l=[]
    while que:
        v=que.popleft()
        l.append(v)
        for nv in G[v]:
            In[nv]-=1
            if In[nv]==0:
                que.append(nv)
    '''
    if len(l)!=P:
        print(-1)
        exit()
    '''
    return l