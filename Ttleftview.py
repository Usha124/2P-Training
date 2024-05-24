class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
def  leftview(root):
    if root==None:
        return 
    result=[]
    q=[root]
    while q: #len(q)
        n=len(q)
        for i in range(n):
            tempnode=q.pop(0)
            if i==0:
                result.append(tempnode.data)
            if tempnode.left != None:
                 q.append(tempnode.left)
            if tempnode.right != None:
                q.append(tempnode.right)
    print(result) 
obj1=Node(90)
obj2=Node(80)
obj3=Node(70)
obj4=Node(60)
obj5=Node(50)
obj6=Node(40)
obj1.left=obj2
obj1.right=obj3
obj2.left=obj4
obj3.left=obj5
obj3.right=obj6
leftview(obj1)