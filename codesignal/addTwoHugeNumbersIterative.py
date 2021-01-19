import collections


# Singly-linked lists are already defined with this interface:
class ListNode(object):
    def __init__(self, x):
        self.value = x
        self.next = None


def addTwoHugeNumbers(a: ListNode, b: ListNode):
    stack_a = collections.deque()
    while a is not None:
        stack_a.append(a.value)
        a = a.next

    stack_b = collections.deque()
    while b is not None:
        stack_b.append(b.value)
        b = b.next

    carry, head = 0, None
    while carry > 0 or len(stack_a) > 0 or len(stack_b) > 0:
        temp = ListNode(carry)

        if len(stack_a) > 0:
            temp.value += stack_a.pop()

        if len(stack_b) > 0:
            temp.value += stack_b.pop()

        carry, temp.value = temp.value // 10000, temp.value % 10000
        temp.next = head
        head = temp

    return head
