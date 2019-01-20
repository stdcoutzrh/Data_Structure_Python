# -*- coding: utf-8 -*-
#single linked list

class node:
    def __init__(self,data):
        self.data = data
        self.next = None
        
class single_linked_list:
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
            cnode = cnode.next
        self.print_list()
                       
    def insert_tail(self):
        cnode = self.head
        while cnode.next !=None:
            cnode=cnode.next
        cnode.next=node(int(input()))
        self.length=self.length+1
        self.print_list()
        
    def insert_head(self):
        cnode = self.head
        nnode = node(int(input()))
        nnode.next = cnode.next
        cnode.next =nnode
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
        while cnode.data!=value and cnode.next!=None:
            pnode = cnode
            cnode = cnode.next
        if cnode.data == value:
            pnode.next = conde.next
            print("del success")
            del cnode
        else:
            print("del failed,no element == value")
        self.print_list()
        
        
