class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class MyLinkedList:

    def __init__(self):
        self.head = Node(0)
        self.size = 0

    def get(self, index: int) -> int:
        if index < 0 or index >= self.size:
            return -1

        curr = self.head.next

        for _ in range(index):
            curr = curr.next

        return curr.val

    def addAtHead(self, val: int) -> None:
        new_node = Node(val)
        new_node.next = self.head
        self.head = new_node
        self.size += 1

    def addAtTail(self, val: int) -> None:
        new_node = Node(val)

        if self.head is None:
            self.head = new_node
        else:
            current = self.head

            while current.next:
                current = current.next

            current.next = new_node

        self.length += 1

    def addAtIndex(self, index: int, val: int) -> None:
        if index < 0:
            index = 0

        if index > self.length:
            return

        if index == 0:
            self.addAtHead(val)
            return

        new_node = Node(val)
        current = self.head

        for _ in range(index - 1):
            current = current.next

        new_node.next = current.next
        current.next = new_node
        self.length += 1

    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or index >= self.length:
            return

        if index == 0:
            self.head = self.head.next
        else:
            current = self.head

            for _ in range(index - 1):
                current = current.next

            current.next = current.next.next

        self.length -= 1
        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)



# 206. Reverse Linked List
class Solution:
    def reverseList(self, head: ListNode | None) -> ListNode | None:
        prev = None
        Curr = head
        while Curr is not None:
            nextNode = Curr.next
            Curr.next = prev
            prev = Curr
            Curr = nextNode
        return prev   
    
    
    
# 876. Middle of the Linked List    
class Solution:
    def middleNode(self, head: ListNode | None) -> ListNode | None:
        slow = head
        fast = head
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
        return slow 
    
    
#   21. Merge Two Sorted Lists  
class Solution:
    def mergeTwoLists(self, list1: ListNode | None, list2: ListNode | None) -> ListNode | None:
        dummy = ListNode()
        tail = dummy
        while list1 is not None and list2 is not None:
            if list1.val <= list2.val:
                tail.next = list1
                list1=list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next
        if list1 is not None:
            tail.next = list1
        else:
            tail.next = list2
        return dummy.next   
        
        

# 2. Add Two Numbers
class Solution:
    def addTwoNumbers(self, l1: ListNode | None, l2: ListNode | None) -> ListNode | None:
        dummy = listNode()
        tail = dummy
        carry = 0
        while l1 is not None and l2 is not None or carrt!=0:
            x=0
            y=0
            if l1 is not None:
                x = l1.val
                l1 = l1.next
            if l2 is not None:
                y= l2.val
                l2 = l2.next
            total = x+y+carry
            digit = total%10
            carry = total//10
            tail.next = ListNode(digit)
            tail=tail.next
        return dummy.next