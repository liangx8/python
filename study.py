class IntegerIterator:
    def __init__(self,v):
        def gen():
            for x in v:
            	yield x
        self.__gen=gen()
    def __next__(self):
        return next(self.__gen)
class IntegerArray:
    def __init__(self):
        self.__values = list()
    def add(self,i):
        self.__values.append(i)
    def __iter__(self):
        return IntegerIterator(self.__values)

def lesson1():
    ia = IntegerArray()
    ia.add(1)
    ia.add("b")
    ia.add(True)
    ia.add(100)
    for i in ia:
        print(i)
        

def full(root):
    import os
    import os.path
    whole=os.listdir(root)
    for one in whole:
        strType="file"
        fpath=os.path.join(root,one)
        if os.path.isdir(fpath):
            strType="dir"
        print(strType,one)

def lesson2(root):
    full(root)

if __name__ == "__main__":
    lesson2("/home/arm")
