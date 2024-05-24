class Tree:
    def __init__(self,data):
        self.val=data
        self.left=None
        self.right=None 
def insertinbst(root,data):
    if root is None:
        return Tree(data)
    else:
        if root.val == data:
            return Tree(data)
        elif root.val>data:
            root.left=insertinbst(root.left,data)
        else:
            root.right=insertinbst(root.right,data)
    return root
def inorder(root):
    if root is None:
        return None 
    inorder(root.left)
    print(root.val,end=" ")
    inorder(root.right)
    return root
obj=Tree(10)
obj=insertinbst(obj,8)
obj=insertinbst(obj,15)
obj=insertinbst(obj,22)
obj=insertinbst(obj,28)
obj=insertinbst(obj,-5)
obj=insertinbst(obj,6)
obj=insertinbst(obj,7)
inorder(obj)




















    