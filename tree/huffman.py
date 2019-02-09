# -*- coding: utf-8 -*-

class huffmanNode(object):
    def __init__(self):
        self.data = '#'
        self.weight = -1
        self.parent=None
        self.leftChild=None
        self.rightChild=None
        
class huffman_tree(object):
    def create(self,nodes):
        TreeNode = nodes[:]
        if len(TreeNode)>0:
            while len(TreeNode)>1:
                lnode = TreeNode.pop(0)
                rnode = TreeNode.pop(0)
                newNode = huffmanNode()
                newNode.leftChild=lnode
                newNode.rightChild=rnode
                newNode.weight=lnode.weight+rnode.weight
                lnode.parent = newNode
                rnode.parent = newNode
                self.insert(TreeNode,newNode)
            return TreeNode[0]
        
    def insert(self,TreeNode,newNode):
        if len(TreeNode)>0:
            tmp = 0
            while tmp<len(TreeNode):
                if TreeNode[tmp].weight>newNode.weight:
                    TreeNode.insert(tmp,newNode)
                    return
                tmp=tmp+1
        TreeNode.append(newNode)
        
    def encoding(self,root,nodes,codes):
        index = range(len(nodes))
        for item in index:
            tmp = nodes[item]
            tcode = ''
            while tmp is not root:
                if tmp.parent.leftChild is tmp:
                    tcode = '0'+tcode
                else:
                    tcode = '1'+tcode
                tmp=tmp.parent
            codes.append(tcode)
            
    def create_leaf_nodes(self,LeafNodes):
        NodeIndormation = input('->').split(' ')
        while NodeIndormation[1] is not '#':
            newnode=huffmanNode()
            newnode.data=NodeIndormation[0]
            newnode.weight=int(NodeIndormation[1])
            LeafNodes.append(newnode)
            NodeIndormation=input('->').split()
        
        
        
        
        
        
        
            
            