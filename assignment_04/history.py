


class History(object):
    def __init__(self):
        pass
    
    def __str__(self):
        str_undo_stack = '[]'
        str_redo_stack = '[]'
        if self._stack_undo:
            str_undo_stack = ''.join(['[%s]'%(st) for st in self._stack_undo])        
        if self._stack_redo:
            str_redo_stack = ''.join(['[%s]'%(st) for st in self._stack_redo])        
        return "CURRENT: %s\nUNDO: %s\nREDO: %s"%(self.current_state,
                                                  str_undo_stack,
                                                  str_redo_stack)

    @property
    def current_state(self):
        pass
    
    def append(self, state):
        pass
    
    def undo(self):
        pass
    
    def redo(self):
        pass       
    
    def clear(self):
        pass