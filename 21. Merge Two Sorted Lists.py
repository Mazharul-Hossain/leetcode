# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def swap_l2(self, l1: ListNode, l2: ListNode):
        # l2 is larger  
        temp1 = l1.next
        temp2 = l2.next
        
        temp_val = l1.val

        l1.val = l2.val
        l2.val = temp_val 
        l1.next = l2
        l1.next.next = temp1

        return l1.next, temp2


    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1 is None:
            return l2
        elif l2 is None:
            return l1
        head = l1
            
        while(l1 is not None and l2 is not None):
            if l1.val <= l2.val:
                if l1.next is None:
                    l1.next = l2
                    break
                l1 = l1.next
            else :
                l1, l2 = self.swap_l2(l1, l2)
                if l2 is None:
                    break
        return head

