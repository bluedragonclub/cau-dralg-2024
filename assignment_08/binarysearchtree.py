
class Node:
    def __init__(self,
                 data=None,
                 left=None,
                 right=None,
                 parent=None):

        pass
        
    def __str__(self):
        return "Node({})".format(self.data)
    
    def __repr__(self):
        return str(self)

    def count_children(self):
        pass
    
    def children(self):
        pass
 

class BinarySearchTree:
    def __init__(self):
        pass
    
    def __len__(self):
        pass
    
    def empty(self):
        pass
    
    def insert(self, data):        
        pass
    
    def inorder(self, get_node=False):
        pass
    
    def preorder(self, get_node=False):
        pass
    
    def postorder(self, get_node=False):
        pass
    
    def min(self, root=None, get_node=False):
        pass
    
    def max(self, root=None, get_node=False):
        pass       
        
    def search(self, data):
        pass

    def remove(self, data):
        pass
    
    def clear(self):
        pass
