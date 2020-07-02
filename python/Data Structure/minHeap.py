class minHeap:
    def __init__(self):
        self.heap=[]
    def heapify(self):
        if not self.heap:
            return
        for i in range(len(self.heap)//2-1,-1,-1):
            if i*2+1<len(self.heap) and self.heap[i*2+1]<self.heap[i]:
                j=i*2+1
            else:
                j=i
            if i*2+2<len(self.heap) and self.heap[i*2+2]<self.heap[j]:
                j=i*2+2
            self.heap[i], self.heap[j] = self.heap[j], self.heap[i]
    def insert(self, x):
        self.heap.append(x)
        self.heapify()
    def extractMin(self):
        if not self.heap:
            return
        temp=self.heap[0]
        self.heap=self.heap[1:]
        self.heapify()
        return temp
obj=minHeap()
obj.insert(2)
obj.insert(3)
obj.insert(1)
obj.insert(-1)
obj.insert(5)
obj.insert(-2)
print(obj.heap)
obj.insert(-3)
print(obj.extractMin())
print(obj.heap)