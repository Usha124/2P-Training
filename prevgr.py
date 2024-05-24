def nextgreatele(nums):
    stack=[]
    n=len(nums)
    result=[-1]*n 
    for i in range(0,n-1):
        while len(stack)>0 and stack[0]<nums[i]:
            stack.pop(0)
        if len(stack)>0:
            result[i]=stack[0]
        stack.insert(0,nums[i])
    return result 
nums=[12,4,67,3,56,78,92]
result=nextgreatele(nums)
print(result) 