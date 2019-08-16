from LinkedList import *

class Tree():
    def __init__(self):
        self.root = LinkedList()
        
    def add(self,value):
        parent = self.root
        self.addIn(value,parent)

    def addIn(self,value,parent):
        parent.add(value)    
