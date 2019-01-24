# -*- coding: utf-8 -*-
class stack_node:
    def __init__(self):
        self.data = None
        self.next = None
        
class linked_stack:
    def __init__(self):
        self.base = stack_node()
        self.top = None
        self.len = 0
        
    def is_empty(self):
        if self.len == 0:
            return True
        else:
            return False
        
    def length(self):
        return self.len
    
    def print_stack(self):
        if self.len == 0:
            print("stack empty!")
            return
        else:
            cnode = self.base
            while cnode.next != None:
                cnode=cnode.next
                print(cnode.data,end=' ')
        
    def push(self,x):
        if self.is_empty():
            nnode = stack_node()
            nnode.data=x
            nnode.next=self.base.next
            self.base.next=nnode
            self.top =nnode
            self.len =self.len+1
        else:
            nnode = stack_node()
            nnode.data=x
            nnode.next=self.top.next
            self.top.next=nnode
            self.top =nnode
            self.len =self.len+1
            
    def pop(self):
        if self.is_empty():
            print("stack empty!")
            return
        else:
            value =self.top.data
            cnode = self.base
            while cnode.next != self.top:
                cnode=cnode.next
            self.top = cnode
            cnode.next =None
            self.len = self.len-1
            return value
        
        

