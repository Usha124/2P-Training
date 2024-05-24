class Queue:
    def __init__(self,c):
        self.c=c
        self.queue=[]
        self.front=self.rear=0
    def enqueue(self,data):
        if self.c==self.rear:
            print("\nqueue is full")
        else:
            self.queue.append(data)
            self.rear=self.rear+1
    def dequeue(self):
        if self.front == self.rear :
            print("\nqueue is empty")
        else:
            a=self.queue.pop(0)
            self.rear=self.rear-1 
    def display(self):
        if self.rear == self.front:
            print("\nqueue is empty")
        else:
            for i in self.queue:
                print(i,end=" ")
    def frontele(self):
        if self.front == self.rear:
            print("\nqueue is empty")
        print("\n",self.queue[self.front])
q=Queue(3)
q.enqueue(20)
q.enqueue(30)
q.enqueue(40)
q.display()
q.enqueue(40)
q.dequeue()
q.display()
q.frontele()
