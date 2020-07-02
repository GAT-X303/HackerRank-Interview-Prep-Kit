import LC21

def main ():
    print("This is my Python test program!")

    list1 = [1, 2 ,4]
    list2 = [1, 3, 4]

    l1 = LC21.ListNode(None, None)
    l2 = LC21.ListNode

    l1Ptr = l1
    l2Ptr = l2

    for num in list1:
        l1Ptr.val = num
        l1Ptr.next = LC21.ListNode(None, None)
        l1Ptr = l1Ptr.next

    for num in list2:
        l2Ptr.val = num
        l2Ptr.next = LC21.ListNode(None, None)
        l2Ptr = l2Ptr.next

    l3 = LC21.mergeTwoLists(l1, l2)

    print(l3.val)
    l3 = l3.next

    print(l3.val)
    l3 = l3.next

    print(l3.val)
    l3 = l3.next

    print(l3.val)
    l3 = l3.next

    print(l3.val)
    l3 = l3.next

    print(l3.val)
    l3 = l3.next
if __name__ == "__main__":
    main()
