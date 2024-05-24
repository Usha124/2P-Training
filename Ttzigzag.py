class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
def zigzag(root):
    if root == None:
        return 
    result=[]
    q=[root]
    level=0
    while len(q)>0:
        n=len(q)
        subres=[]
        for i in range(n):
            tempNode=q.pop(0)
            subres.append(tempNode.data)
            if (tempNode.left != None):
                q.append(tempNode.left)
            if (tempNode.right != None):
                q.append(tempNode.right)
            if level%2 ==0:
                subres.reverse()
            level+=1
        result.append(subres)
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
zigzag(obj1)
            