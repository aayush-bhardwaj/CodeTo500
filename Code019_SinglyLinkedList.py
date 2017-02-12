class Node:
    def __init__(self):
        self.data = None
        self.next = None

    def setData(self, data):
        self.data = data

    def getData(self):
        return self.data

    def setNext(self, next):
        self.next = next

    def getNext(self):
        return self.next


class LinkedList:
    def __init__(self):
        self.head = None
        self.len = 0

    def insertAtBeginning(self, data):
        #import pdb;pdb.set_trace()
        newNode = Node()

        newNode.setData(data)
        if(self.len == 0):
            self.head = newNode
        else:
            newNode = self.head
            self.head = newNode
        self.len += 1

    def insertAtEnd(self, data):

        newNode = Node()
        newNode.setData(data)
        curr = self.head
        while(curr.getNext() != None):
            curr = curr.getNext()
        curr.setNext(newNode)
        self.len += 1

    def insertPosition(self, data, position):
        newNode = Node()
        newNode.setData(data)
        #import pdb;pdb.set_trace()
        curr = self.head
        if(position == 0):
            insertAtBeginning(data)
        if(position == (self.len -1)):
            insertAtEnd(data)
        else:

            pos = 0
            while(pos < (position-1)):
                curr = curr.getNext()
                pos += 1
            newNode.setNext(curr.getNext())
            curr.setNext(newNode)
            self.len += 1

    def parseList(self):
        #import pdb;pdb.set_trace()
        curr = self.head
        while(curr != None):
            data = curr.getData()
            nexta = curr.getNext()
            print("%s - %s" %(data, nexta))
            curr = curr.getNext()

    def reverseList(self):
        curr = self.head
        while(curr.getNext() != None):
            #import pdb;pdb.set_trace()
            if(curr == self.head):
                nexta = curr.getNext()
                curr.setNext(None)
                prev = curr
                curr = nexta
            else:
                nexta = curr.getNext()
                curr.setNext(prev)
                prev = curr
                curr = nexta
                if(nexta.getNext() == None):
                    self.head = nexta
                    curr.setNext(prev)
                    break
                nexta = nexta.getNext()




obj = LinkedList()
obj.insertAtBeginning(1)
#obj.parseList()
obj.insertAtEnd(2)
obj.insertAtEnd(4)
obj.insertAtEnd(5)
obj.insertPosition(3,2)
obj.parseList()

obj.reverseList()
obj.parseList()
