class Node:
    def __init__(self,item=None,next=None):
        self.item=item 
        self.next=next 
class Stack:
    def __init__(self):
        self.start=None
        self.items_count=0
    def is_empty(self):
        return self.start==None 
    def push(self,data):
        n=Node(data,self.start)
        self.start=n 
        self.items_count+=1
    def pop(self):
        if not self.is_empty():
            data=self.start.item 
            self.start=self.start.next 
            self.items_count-=1
            return data 
        else:
            raise IndexError("stack is empty")
    def peek(self):
        if not self.is_empty():
            return self.start.item 
        else:
            raise self.is_empty()
    def size(self):
        return self.items_count
s=Stack()
s.push(10)
s.push(30)
s.push(50)
print(s.peek())
print(s.pop())
print(s.peek())
print(s.size())
            
            
            