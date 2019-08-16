from Node import *
from Compare import *

class LinkedList():
    def __init__(self):
        self.first = None
         

    def add(self,value):
        if(not self.first):
            self.first = Node(value)
        else:
            compare = Compare()
            if(compare.compare(self.first,value) > 0):
                stack = self.first
                self.first = Node(value)
                self.first.next = stack
                return True
            elif(compare.compare(self.first,value) == 0):
                stack = self.first.next
                self.first = Node(value)
                self.first.next = stack
                return True
            else:
                previous = self.first
                current = self.first.next
                while(current):
                    if(compare.compare(current,value) < 0):
                        previous = current
                        current = current.next
                        return True
                    elif(compare.compare(current,value) > 0):
                        previous.next = Node(value)
                        previous.next.next = current
                        return True
                    else:
                        stack = current.next
                        previous.next = Node(value)
                        previouos.next.next = stack
                        return True
            previous.next = Node(value)
            return True                        

