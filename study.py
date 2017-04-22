class IntegerIterator:
	def __init__(self,v):
		def gen():
			for x in v:
				yield x
		self.__gen=gen()
#	def __iter__(self):
#		print(self.__index)
#		return self
	def __next__(self):
		return next(self.__gen)
class IntegerArray:

	def __init__(self):
		self.__values = list()
	def add(self,i):
		self.__values.append(i)
	def __iter__(self):
		return IntegerIterator(self.__values)
if __name__ == "__main__":
    ia = IntegerArray()
    ia.add(1)
    ia.add("b")
    ia.add(True)
    ia.add(100)
    for i in ia:
        print(i)
