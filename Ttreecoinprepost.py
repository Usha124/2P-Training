class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None 
def inorder(root):
    if root == None:
        return None
    inorder(root.left)
    print(root.data,end= ' ')
    inorder(root.right)
def preorder(root):
    if root==None:
        return None 
    print(root.data,end=" ")
    preorder(root.left)
    preorder(root.right)
def postorder(root):
    if root==None:
        return None 
    postorder(root.left)
    postorder(root.right)
    print(root.data,end=" ")
    
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
print(obj1.data)
print(obj1.right.data)
inorder(obj1)
print()
preorder(obj1)
print()
postorder(obj1)
print()