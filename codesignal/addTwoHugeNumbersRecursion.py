# https://www.geeksforgeeks.org/python-handling-recursion-limit/
# importing the sys module
import sys

# the setrecursionlimit function is
# used to modify the default recursion
# limit set by python. Using this,
# we can increase the recursion limit
# to satisfy our needs
sys.setrecursionlimit(10 ** 6)


# Singly-linked lists are already defined with this interface:
class ListNode(object):
    def __init__(self, x):
        self.value = x
        self.next = None


def find_length(a):
    if a is None:
        return 0
    elif a.next is None:
        return 1
    else:
        return 1 + find_length(a.next)


def rec_add(a, b):
    if a is None:
        return 0, b
    if b is None:
        return 0, a

    carry, a.next = rec_add(a.next, b.next)
    a.value = a.value + b.value + carry

    carry, a.value = a.value // 10000, a.value % 10000
    return carry, a


def addTwoHugeNumbers(a, b):
    len_a = find_length(a)
    len_b = find_length(b)

    if len_b > len_a:
        temp = a
        a = b
        b = temp

        diff = len_b - len_a
    else:
        diff = len_a - len_b

    while (diff > 0):
        temp = ListNode(0)
        temp.next = b
        b = temp

        diff -= 1

    carry, a = rec_add(a, b)
    if carry > 0:
        temp = ListNode(carry)
        temp.next = a
        a = temp
    return a
