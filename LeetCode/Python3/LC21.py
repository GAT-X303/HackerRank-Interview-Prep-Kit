"""
LeetCode Problem - 21
"""
import random

class Node:
    def __init__(self, data, next):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self, head):
        self.head = head        

def mergeTwoLists(l1, l2):
    l3 = LinkedList

def createdRandomLinkedList(size):
    unsortedLinkedList = LinkedList(None)

    unsortedLinkedList.head = Node(random.randint(0,9), None)
    currentNode = unsortedLinkedList.head

    for i in range(size-1):
        currentNode.next = Node(random.randint(0,9), None)
        currentNode = currentNode.next

    return unsortedLinkedList

def printLinkedList(linkedList):
    currentNode = linkedList

    output = []

    output.append(currentNode.head.data)

    currentNode = currentNode.head.next

    while currentNode.next!= None:
        output.append(currentNode.data)
        currentNode = currentNode.next
    
    print(output)
