# -*- coding: utf-8 -*-

#双亲表示法结点
class treeNode_1(object):
    def __init__(self):
        self.data = '#'
        self.parent = '-1'
        
#孩子表示法结点
class treeNode_2(object):
    def __init__(self):
        self.data = '#'
        self.firstChild = None
        
class childNode(object):
    def __init__(self):
        self.index=-1
        self.nextSibling = None
        
#孩子兄弟表示法结点
class treeNode_3(object):
    def __init__(self):
        self.data = '#'
        self.pFirstChild = None
        self.pNextSibling = None
        

        
