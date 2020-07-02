"""
LeetCode Problem - 21
Allan Hieng
"""

class ListNode:
    def __init__(self, val=0, next = None):
        self.val = val
        self.next = next

def mergeTwoLists(l1, l2):
    print("Merging Lists!")

    l3 = ListNode(None, None)
    l3Ptr = l3

    while l1.next is not None or l2.next is not None:
        if l1.val == l2.val:
            l3Ptr.val = l1.val
            l1 = l1.next

            l3Ptr.next = ListNode(None, None)
            l3Ptr = l3Ptr.next

            l3Ptr.val = l2.val
            l2 = l2.next
        elif l1.val < l2.val:
            l3Ptr.val = l1.val
            l1 = l1.next
        elif l1.val > l2.val:
            l3Ptr.val = l2.val
            l2 = l2.next

        l3Ptr.next = ListNode(None, None)
        l3Ptr = l3Ptr.next

    return(l3)

def printLinkedList(linkedList):
    print("Printing linked list...")
    while linkedList.next is not None:
        print(linkedList.val)
        linkedList = linkedList.next