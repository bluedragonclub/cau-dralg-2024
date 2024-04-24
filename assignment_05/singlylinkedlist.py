
class Node(object):
    
    def __init__(self, data=None):
        pass
    
    
class SinglyLinkedList(object):
    
    def __init__(self):
        pass
        
    def __str__(self):
        if self.empty():
            return "[]"
        else:
            tmp_list = []  # Temporary list of strings
            cur = self._head            
            while cur != None:
                tmp_list.append("[%s]"%(cur.data))
                cur = cur.next
        
            return "->".join(tmp_list)
        
    def __len__(self):
        pass 
            
    def empty(self):
        pass
        
    def insert(self, i, data):
        pass

    def remove(self, i):
        pass
              
    def clear(self):
        pass
    
    def get(self, i):
        pass
    
    def pop(self, i=None):
        pass
    
    def search(self, target, start=0):
        pass

    def extend(self, sll):
        pass
  
