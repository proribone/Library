#平衡二分木の代用

from heapq import heapify,heappop,heappush
class mset:
    def __init__(self):
        self.p,self.q,self.dic=[],[],{}
        heapify(self.p);heapify(self.q)
    def add(self,a):
        heappush(self.p,a)
        if not a in self.dic:
            self.dic[a]=1
        else:
            self.dic[a]+=1
    def delete(self,a):
        if a in self.dic and self.dic[a]>0:
            heappush(self.q,a)
            self.dic[a]-=1
    def search(self,a):
        return a in self.dic
    def minimum(self):
        while self.q and self.p[0]==self.q[0]:
            heappop(self.p);heappop(self.q)
        return self.p[0] if self.p else None


#軽量版
class mset_:
    def __init__(self):
        self.p,self.q=[],[]
        heapify(self.p);heapify(self.q)
    def add(self,a):
        heappush(self.p,a)
    def delete(self,a):
        heappush(self.q,a)
    def minimum(self):
        while self.q and self.p[0]==self.q[0]:
            heappop(self.p);heappop(self.q)
        return self.p[0] if self.p else None