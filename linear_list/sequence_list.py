# -*- coding: utf-8 -*-
#线性表的顺序存储
class seqlist:
    def __init__(self):
        self.seqlist = []
        
    def create_list(self,n):
        for i in range (n):
            self.seqlist.append(int(input()))
        print(self.seqlist)

    def length(self):
        return len(self.seqlist)

    def locate_element(self,e):
        i = 0
        while i<len(self.seqlist):
            if self.seqlist[i]==e:
                print(i)
                break
            i=i+1
        if i==len(self.seqlist):
            print("no e in list")
   
    def get_element(self,i):
        if i>=len(self.seqlist) or i<0:
            print("error para")
        else:
            print(self.seqlist[i])
   
    def insert(self,i,e):
        self.seqlist.insert(i,e)
        print(self.seqlist)

    def delete(self,i):
        self.seqlist.remove(self.seqlist[i])
        print(self.seqlist)

    def print_list(self):
        print(self.seqlist)

    def is_empty(self):
        if len(self.seqlist) ==0:
            print("List is empty")
        else:
            print("List is not empty")

    def __del__(self):
        pass



