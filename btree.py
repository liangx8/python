import tree.view

class Node:
##    @staticmethod
##    def newNode(value):
##        obj=Node()
##        obj.value=value
##        obj.balance=0
##        return obj
    def __init__(self,value):
        self.left=None
        self.right=None
        self.bal=0
        self.value=value
def toViewModel(src):
    if src.right:
        children = (src.left,src.right)
        src.children=children
    else:
        if src.left:
            children = (src.left)
            src.children=children
    if src.right:
        toViewModel(src.right)
    if src.left:
        toViewModel(src.left)
    
def recursAdd(root,value,cmp):
    cp = cmp(value,root.value)
    if cp<0 :
        
        if root.left:
            nleft,inc = recursAdd(root.left,value,cmp)
            root.left=nleft
            if inc :
                root.bal = root.bal - 1
                
        else:
            root.left=Node(value)
            root.bal = root.bal -1
            if root.right:
                return root,False
            else:
                return root,True
            
    else:
        if root.right:
            nright,inc = recursAdd(root.right,value,cmp)
            root.right=nright
            if inc:
                root.bal = root.bal +1
        else:
            root.right=Node(value)
            root.bal = root.bal +1
            if root.left:
                return root,False
            else:
                return root,True
    return doBalance(root),False
def doBalance(top):
    return top
class Btree:
    def __init__(self,cmp):
        self.__cmp=cmp
        self.__root=None
    def viewModel(self):
        toViewModel(self.__root)
        return self.__root
    def add(self,value):
        
        if self.__root :
            top,_=recursAdd(self.__root,value,self.__cmp)
            self.__root=top
        else:
            self.__root=Node(value)
##         c                     a 
##        / \                   / \
##       a   ?                 ?   c
##      / \               =>   |  / \
##     ?   b                   ? b   ?
##     |
##     ?
def rotate_right(top):
    c = top
    a = top.left
    b = top.left.right
    a.right=c
    c.left=b
    c.bal=0
    a.bal=0
    return a
##         a                        c 
##        / \                      / \
##       ?   c                    a   ?
##          / \               => / \  |
##         b   ?                ?   b ?
##             |
##             ?
def rotate_left(top):
    a = top
    c = top.right
    b = top.rigth.left
    a.right=b
    c.left=a
    c.bal=0
    a.bal=0
    return c
if __name__ == '__main__':
    def cmp(l,r):
        return l-r
    def r(v):
        print("run value: %d" % v)

    b=Btree(cmp)
    b.add(3)
    b.add(2)
    b.add(1)
    def asStr(o):
        return o
    print(tree.view.textView(b.viewModel(),2,asStr))
