class Queue:
    def __init__(self):
        self.item=[]
    def is_empty(self):
        return len(self.item)==0
    def push(self,data):
        self.item.append(data) 
    def pop(self):
        if not self.is_empty():
            self.item.pop()
        else:
            raise IndexError("stack is empty")
    def peek(self):
        if not self.is_empty():
            return self.item[-1]
        else:
            raise IndexError("stack is empty")
    def size(self):
        return len(self.item)
q1=Queue()
q1.push(10)
q1.push(30)
q1.push(50)
print(q1.peek())
q1.pop()
print(q1.peek())