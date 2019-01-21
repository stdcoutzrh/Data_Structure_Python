# -*- coding: utf-8 -*-
#circular double linked list

class node:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None
        
class circular_double_linked_list:
    def __init__(self):
        self.head = node(None)
        self.length = 0
        
    def length(self):
        return self.length
       
    def print_list(self):
        cnode = self.head.next
        for i in range(self.length):
            print(cnode.data)
            cnode=cnode.next 
            
    def create(self,n):
        cnode = self.head
        self.length = n
        for i in range(n):
            nnode = node(int(input()))
            cnode.next = nnode
            nnode.prev = cnode
            nnode.next=self.head
            self.head.prev=nnode
            cnode = cnode.next
        self.print_list()
                       
    def insert_tail(self):
        cnode = self.head
        while cnode.next !=self.head:
            cnode=cnode.next
        nnode=node(int(input()))
        cnode.next=nnode
        nnode.prev=cnode
        nnode.next=self.head
        self.head.prev=nnode
        self.length=self.length+1
        self.print_list()
        
    def insert_head(self):
        cnode = self.head.next
        pnode = self.head
        nnode = node(int(input()))
        nnode.prev = pnode
        pnode.next = nnode
        nnode.next = cnode
        cnode.prev=nnode
        self.length=self.length+1
        self.print_list()
        
    def get_element(self,e):
        pos = 0
        cnode = self.head
        if self.length == 0:
            print("not found!")
            return 
        while cnode.data!=e and cnode.next!=None:
            cnode = cnode.next
            pos = pos+1
        if cnode.data == e:
            print("found element :",pos)
        else:
            print("not found")
        self.print_list()
            
    def delete_element(self,value):
        cnode = self.head
        pnode = self.head
        if self.length == 0:
            print("not found!")
            return 
        while cnode.data!=value and cnode.next!=self.head:
            pnode = cnode
            cnode = cnode.next
        if cnode.data == value:
            qnode=cnode.next
            pnode.next=qnode
            qnode.prev=pnode
            del cnode
            print("del success") 
        else:
            print("del failed,no element == value")
        self.print_list()
        
        
