# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def printList(self, head: ListNode) -> None:
        result_string = ""
        while head is not None:
            result_string += str(head.val) + " "
            head = head.next
        print(result_string)

    def oddEvenList(self, head: ListNode) -> ListNode:
        if head is None or head.next is None:
            return head 
        root, even = head, head.next
        while even is not None and even.next is not None:
            temp = head.next
            
            head.next = even.next
            head = head.next            
            
            even.next = head.next
            even = even.next    
            head.next = temp

            self.printList(root)
        return root