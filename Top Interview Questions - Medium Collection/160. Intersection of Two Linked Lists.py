# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getDistance(self, head: ListNode):
        length = 0
        while head is not None and head.next is not None:
            if head.next is not None:
                length += 1
                head = head.next
        return length, head

    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        lengthA, tempA = self.getDistance(headA)
        lengthB, tempB = self.getDistance(headB)

        if tempA != tempB:
            return None
        
        if lengthB > lengthA:
            temp_l = lengthB - lengthA
            while temp_l > 0:
                temp_l -= 1
                headB = headB.next
        else:
            temp_l = lengthA - lengthB
            while temp_l > 0:
                temp_l -= 1
                headA = headA.next
        
        while headA != headB:
            headA, headB = headA.next, headB.next
        return headA
