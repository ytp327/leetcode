# stack: first in last out
# implement stack using list in python
stack=[]
def push(stack, x):
    try:
        stack.append(x)
        return True
    except:
        return False
def pop(stack):
    try:
        return stack.pop()
    except:
        return -1
push(stack,2)
print(pop(stack))