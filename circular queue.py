#OCR A Level Computer Science Topic 2 queues
#circularQueue.py demonstrates enqueuing and dequeuing items
#from a circular queue

#constructing a queue ADT
class CircularQueue:
    def __init__(self,maxItems):
        self.items = [None]*maxItems
        self.front = 0
        self.rear = -1
        self.size = 0
        self.maxSize = maxItems
              
    
    def isEmpty(self):
        return self.size == 0
        
    
    def isFull(self):
        print("self.size, self.maxSize",self.size, self.maxSize)
        return self.size == self.maxSize
    
    def enqueue(self, item):
        if self.size == self.maxSize:
            print("queue is full, size =",self.size)
        else:
            self.rear = (self.rear + 1)% (self.maxSize)
            self.size += 1
            self.items[self.rear] = item

    def dequeue(self):
        if (self.size == 0):
            return "Queue empty"
        else:
            first = self.items[self.front]
            self.size -= 1
            self.front = (self.front + 1) % (self.maxSize)
            return first
        
    def size(self):
        return self.size
    
    def show(self):
        print("list and pointers",self.items, self.front,self.rear, "size =",self.size)
     
    def showFront(self):
        print(self.items[0])
        
q = CircularQueue(5)
q.show()
q.enqueue("job1")
q.enqueue("job2")
q.enqueue("job3")
print("job1, job2, job3")
q.show()
q.enqueue("job4")
q.enqueue("job5")
print("job1,job2,job3, job4, job5")
q.show()
q.enqueue("jobFull")
q.showFront()
q.dequeue()
q.dequeue()
q.dequeue()
print("job4,job5")
q.enqueue("job6")
q.enqueue("job7")
q.show()
q.dequeue()
q.dequeue()
q.dequeue()
q.dequeue()
q.show()
q.dequeue()
print(q.dequeue())
