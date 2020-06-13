# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        carry, sum, head = 0, 0, l1

        while l1 is not None and l2 is not None:
            sum = l1.val + l2.val + carry
            carry = sum // 10
            l1.val = sum % 10

            if l1.next is None:
                if carry > 0:
                    l1.next = ListNode(val=carry)
                    carry = 0
                else:
                    l1.next = l2.next
                    break
            elif l2.next is None:
                if carry > 0:
                    l2.next = ListNode(val=carry)
                    carry = 0
                else:
                    break
            l1, l2 = l1.next, l2.next
        return head