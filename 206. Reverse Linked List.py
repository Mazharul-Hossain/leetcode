# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        my_stack = []
        if head is None or head.next is None:
            return head
        my_stack.append(head.next)
        head.next = None
        while my_stack:
            temp = my_stack.pop()
            if temp.next is not None:
                my_stack.append(temp.next)
            temp.next = head
            head = temp
        return head