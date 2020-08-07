class bitset:
    def __init__(self,s):
        self.b=int(s,2)
        self.pcnt=s.count('1')
        
    def merge(self,x,y):
        self.b=x.b|y.b
        self.pcnt=bin(self.b).count('1')
        
    def add(self,x):
        self.b|=1<<x
        self.pcnt+=1
        
    def remove(self,x):
        self.b^=1<<x
        self.pcnt-=1

    def popcount(self):
        return self.pcnt

    def isin(self,x):
        return self.b>>x&1
    
class M_bitset:
    def __init__(self,minimum):
        self.b=0
        self.pcnt=0
        self.minimum=abs(minimum)
        
    def merge(self,x,y):
        self.b=x.b|y.b
        self.pcnt=bin(self.b).count('1')
        
    def add(self,x):
        self.b|=1<<(x+self.minimum)
        self.pcnt+=1
        
    def remove(self,x):
        self.b^=1<<(x+self.minimum)
        self.pcnt-=1

    def popcount(self):
        return self.pcnt

    def isin(self,x):
        return self.b>>(x+self.minimum)&1
