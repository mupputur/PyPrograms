class Node:

    def __init__(self,  data, nextNode=None):
        self.data = data
        self.next = nextNode

    def getData(self):
        return self.data

    def setData(self, val):
        self.data = val

    def getNextNode(self):
        return self.next

    def setNextNode(self, val):
        self.next = val

class LinkedList:

    def __init__(self, head=None):
        self.head = head
        self.size = 0

    def getSize(self):
        return self.size

    def addNode(self, data):
        newNode = Node(data)

