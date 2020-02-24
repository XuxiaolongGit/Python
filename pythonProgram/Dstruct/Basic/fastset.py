"使用字典将集合性能优化为线性的"

import set
class Set(set.Set):
    def __init__(self,value = []):
        self.data = {}
        self.concat(value)

    def intersect(self,other):
        res = {}
        for x in other:
            if x in self.data:
                res[x] = None
        return Set(res.keys())

    def union(self,other):
        res = {}
        for x in other:
            res[x] = None
        for x in self.data.keys():
            res[x] = None
        return Set(res.keys())

    def concat(self,value):
        for x in value:
            self.data[x]=None

    # 继承and、or和len方法
    def __getitem__(self,ix):
        return list(self.data.keys())[ix]

    def __repr__(self):
        return '<Set:%r>'% list(self.data.keys())
