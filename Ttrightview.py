class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
def rightview(root):
    if root == None:
        return 
    result=[]
    q=[root]
    while len(q):
        n=len(q)
        for i in range(n):
            tempnode=q.pop(0)
            if i == n-1:
                result.append(tempnode.data)
            if tempnode.left is not None:
                q.append(tempnode.left)
            if tempnode.right is not None:
                q.append(tempnode.right)
    print(result) 
obj1=Node(4)
obj2=Node(5)
obj3=Node(2)
obj4=Node(3)
obj5=Node(1)
obj6=Node(6)
obj7=Node(7)
obj1.left=obj2
obj1.right=obj3
obj3.left=obj4
obj3.right=obj5
obj4.left=obj6
obj4.right=obj7
rightview(obj1)


            