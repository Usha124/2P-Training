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
def inorder(root,res):
    if root is None:
        return None 
    inorder(root.left,res)
    res.append(root.val)
    inorder(root.right,res)
    return sorted(res)
res=[]
obj=Tree(10)
obj=insertinbst(obj,8)
obj=insertinbst(obj,15)
obj=insertinbst(obj,22)
obj=insertinbst(obj,28)
obj=insertinbst(obj,-5)
obj=insertinbst(obj,6)
obj=insertinbst(obj,7)
k=3
i=inorder(obj,res)
print(i[-k])#largest kth 
print(i[k])#smallest kth



