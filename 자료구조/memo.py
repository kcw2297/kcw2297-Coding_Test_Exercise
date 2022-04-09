import gc

from requests import delete

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def push(self, value):
        newNode = Node(value)
        newNode.next = self.head

        if self.head != None:
            self.head.prev = newNode
        
        self.head = newNode

    def append(self, value):
        newNode = Node(value)


        last = self.head
        while last.next:
            last = last.next

        last.next = newNode
        newNode.prev = last

    def insertAfter(self, prev_node, value):
        newNode = Node(value)

        newNode.next = prev_node.next
        prev_node.next.prev = newNode
        newNode.prev = prev_node
        prev_node.next = newNode

    def deleteNode(self, dele):
        if self.head == dele:
            self.head = self.next

        if dele.next is not None:
            dele.next.prev = dele.next

        if dele.prev is not None:
            dele.prev.next = dele.next

    def reverse(self):
        temp = None
        current = self.head

        while current is not None:
            temp = current.prev
            current.prev = current.next
            current.next = temp
            current = current.prev

        if temp is not None:
            self.head = temp.prev
