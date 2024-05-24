class Node:
    def __init__(self,item=None,next=None):
        self.item=item
        self.next=next 
class Queue:
    def __init__(self):
        self.rear=None
        self.front=None 
        self.items_count=0 
    def is_empty(self):
        return self.items_count==0 
        # return self.front==0
        # return self.rare==0
    def enqueue(self,data):
        n=Node(data)
        if self.is_empty():
            self.front=n
            self.rear=n 
        else:
            self.rear.next=n 
            self.rear=n 
        self.items_count+=1
    def dequeue(self):
        if self.is_empty():
            raise IndexError("Empty Queue")
        elif self.front==self.rear:
            self.rear=None 
            self.front=None
        else:
            self.front=self.front.next 
        self.items_count-=1
    def get_front(self):
        if self.is_empty():
            raise IndexError("empty queue")
        else:
            return self.front.item 
    def get_rear(self):
        if self.is_empty():
            raise IndexError("empty queue")
        else:
            return self.rear.item 
q1=Queue()
q1.enqueue(10)
q1.enqueue(30)
q1.enqueue(50)
print(q1.get_front(),q1.get_rear())
q1.dequeue()
print(q1.get_front(),q1.get_rear())
            
            
            
        