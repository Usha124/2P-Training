class Node:
    def __init__(self,item=None,next=None):
        self.item=item
        self.next=next
class SLL:
    def __init__(self,start=None):
        self.start=start
    def is_empty(self):
        return self.start==None
    def in_f(self,data):
        n=Node(data,self.start)
        self.start=n 
    def in_l(self,data):
        n=Node(data)
        if not self.is_empty():
            temp=self.start 
            while temp.next is not None:
                temp=temp.next 
            temp.next=n 
        else:
            self.start=n 
    def search(self,data):
        #if not self.is_empty():
        temp=self.start 
        while temp is not None:
            if temp.item==data:
                return temp
            temp=temp.next
        return None 
    def inaf(self,data,temp):
        if temp is not None:
            n=Node(data,temp.next)
            temp.next=n 
    def printl(self):
        temp=self.start 
        while temp is not None:
            print(temp.item,end=" ")
            temp=temp.next 
    def delf(self):
        if self.start==None:
            pass
        elif self.start is not None:
            self.start=self.start.next 
        else:
            self.start=None 
    def dell(self):
        if self.start is None:
            pass 
        elif self.start.next is None:
            self.start=None 
        else:
            temp=self.start
            while temp.next.next is not None:
                temp=temp.next
            temp.next=None 
    def del_item(self,data):
        if self.start is None:
            pass 
        elif self.start.next is None:
            if self.start.item==data:
                self.start=None 
        else:
            temp=self.start 
            if temp.item==data:
                self.start=self.start.next 
            while temp.next is not None:
                if temp.next.item==data:
                    temp.next=temp.next.next 
                    break 
                    temp=temp.next 
s1=SLL()
s1.in_f(20)
s1.in_f(50)
s1.in_l(60)
s1.inaf(45,s1.search(20))
s1.inaf(55,s1.search(50))
s1.delf()
s1.dell()
s1.del_item(20)
s1.printl()
