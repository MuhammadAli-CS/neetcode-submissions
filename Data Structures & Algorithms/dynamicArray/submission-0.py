class DynamicArray:
    
    def __init__(self, capacity: int):
        self.arr=[None]*capacity
        self.size=0

    def get(self, i: int) -> int:
        return self.arr[i]

    def set(self, i: int, n: int) -> None:
        self.arr[i]=n

    def pushback(self, n: int) -> None:
        if self.size==len(self.arr):
            self.resize()
        self.arr[self.size]=n
        self.size+=1

    def popback(self) -> int:
        self.size-=1
        return self.arr[self.size]


    def resize(self) -> None:
        arr=self.arr
        for i in range(len(self.arr)):
            arr.append(None)

    def getSize(self) -> int:
        return self.size
    
    def getCapacity(self) -> int:
        return len(self.arr)