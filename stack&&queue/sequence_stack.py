# -*- coding: utf-8 -*-
class sequence_stack:
    def __init__(self,MAX_SIZE):
        self.max_size = MAX_SIZE
        self.s = [None for x in range(0,self.max_size)]
        self.top = -1
        
    def length(self):
        return self.top+1
    
    def print_stack(self):
        if self.length() == 0:
            print("stack empty!")
            return
        else:
            for i in range(0,self.length()):
                print(self.s[i],end = ' ')
                
    def is_empty(self):
        if self.length() == 0:
            return True
        else:
            return False
        
    def push(self,x):
        if self.length() == self.max_size:
            print("stack full!")
            return 
        else:
            self.top = self.top+1
            self.s[self.top]=x
            
    def pop(self):
        if self.length() == 0:
            print("stack empty!")
            return
        else:
            vau = self.s[self.top]
            self.top = self.top-1
            return vau
        
    def get_top_value(self):
        if self.length() == 0:
            print("stack empty!")
            return
        else:
            vau = self.s[self.top]
            return vau
        
    
            
        
        
    
        
        
