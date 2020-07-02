# definition
class ListNode:
    def __init__(self, x):
        self.val=x
        self.next=None

class LinkedList:
    def __init__(self):
        self.head=None

# code execution starts here
if __name__ =='__main__':
    llist=LinkedList()
    llist.head=ListNode(1)
    second=ListNode(2)
    third=ListNode(3)
    llist.head.next=second
    second.next=third

    # traverse linked list
    def traverse(node):
        while node:
            print(node.val, end=' ')
            # can replaced by other operation
            node = node.next

    traverse(llist.head)

