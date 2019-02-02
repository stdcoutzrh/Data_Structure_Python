# -*- coding: utf-8 -*-
class sequence_queue:
    def __init__(self,max_size):
        self.max_size = max_size
        self.s=[None for x in range(0,self.max_size)]
        self.front = 0
        self.rear = 0
        self.size=0
        
    def is_empty(self):
        if self.front == self.rear:
            return True
        else:
            return False
        
    def print_queue(self):
        cur = self.front
        for i in range(self.size):
            print(self.s[cur])
            cur=cur+1
            
    def get_head(self):
        if self.is_empty():
            print("queue is empty")
            return
        else:
            return self.s[self.front+1]
        
    def enqueue(self,x):
        if (self.rear+1)%self.max_size!=self.front:
            self.rear = (self.rear+1)%self.max_size
            self.s[self.rear]=x
            self.size=self.size+1
        else:
            print("queue is full")
            return
        
    def dequeue(self):
        if self.is_empty():
            print("empty queue")
            return 
        else:
            self.front=(self.front+1)%self.max_size
            self.size=self.size-1
            return self.s[self.front]
        
    def create(self,n):
        for i in range(n):
            x=input()
            self.enqueue(int(x))