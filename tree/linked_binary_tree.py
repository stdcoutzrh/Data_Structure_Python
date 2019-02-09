# -*- coding: utf-8 -*-

class linked_binary_treeNode(object):
    def __init__(self):
        self.data='#'
        self.leftChild = None
        self.rightChild = None
        
    def visit(self,node):
        if node.data is not '#':
            print(node.data)
        
    def pre_order(self,root):
        if root is not None:
            self.visit(root)
            self.pre_order(root.leftChild)
            self.pre_order(root.rightChild)
            
    def pre_order_nonRec(self,root):
        stack_tree_node = []
        tnode = root
        while len(stack_tree_node)>0 or tnode is not None:
            self.visit(tnode)
            stack_tree_node.append(tnode)
            tnode=tnode.rightChild
        if len(stack_tree_node)>0:
            tnode = stack_tree_node.pop()
            tnode = tnode.rightChild
            
    def in_order(self,root):
        if root is not None:  
            self.pre_order(root.leftChild)
            self.visit(root)
            self.pre_order(root.rightChild)
            
    def in_order_nonRec(self,root):
        stack_tree_node = []
        tnode = root
        while len(stack_tree_node)>0 or tnode is not None:
            while tnode is not None:
                stack_tree_node.append(tnode)
                tnode=tnode.leftChild
            if len(stack_tree_node)>0:
                tnode =stack_tree_node.pop()
                self.visit(tnode)
                tnode = tnode.leftChild
                
    def post_order(self,root):
        if root is not None:            
            self.pre_order(root.leftChild)
            self.pre_order(root.rightChild)
            self.visit(root)
            

        
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            