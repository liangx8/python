class Node:
    def __init__(self,value):
        self.value=value
        self.left=None
        self.right=None
        self.llevel=0
        self.rlevel=0
def recursAdd(root,value,cmp):
    cp = cmp(value,root.value)

    if cp<0 :
        root.llevel=root.llevel + 1
        if root.left:
            recursAdd(root.left,value,cmp)
        else:
            root.left=Node(value)
    else:
        root.rlevel=root.rlevel + 1
        if root.right:
            recursAdd(root.right,value,cmp)
        else:
            root.right=Node(value)

def eachNode(root,run):
    if root:
        if root.left:
            eachNode(root.left,run)
        run(root.value)
        if root.right:
            eachNode(root.right,run)
class Btree:
    def __init__(self,cmp):
        self.__cmp=cmp
        self.__root=None
    def add(self,value):
        if self.__root :
            recursAdd(self.__root,value,self.__cmp)
        else:
            self.__root=Node(value)
    def each(self,run):
        eachNode(self.__root,run)
if __name__ == '__main__':
    def cmp(l,r):
        return l-r
    def r(v):
        print("run value: %d" % v)

    b=Btree(cmp)
    b.add(1)
    b.add(2)
    b.add(3)
    b.each(r)

