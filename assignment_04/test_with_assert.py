from history import History

history = History()

# <Test member variables and property>
assert hasattr(history, '_stack_undo')
assert isinstance(history._stack_undo, list)

assert hasattr(history, '_stack_redo')
assert isinstance(history._stack_redo, list)

assert history.current_state is None
print(history, end='\n\n')

# <Test undo() for empty REDO stack>
"""When undo() is called for an empty UNDO stack,
   the History object do nothing.
"""
history.undo()

# <Test redo() for empty REDO stack>
"""When redo() is called for an empty REDO stack,
   the History object do nothing.
"""
history.redo()


print("<Test append()>")
for i in range(10):
    history.append("ST(#%02d)"%(i+1))
    assert history.current_state == "ST(#%02d)"%(i+1)
    print(history)
print()

print("<Test undo()>")
history.undo()  # Back to ST(#09)
history.undo()  # Back to ST(#08)
history.undo()  # Back to ST(#07)
history.undo()  # Back to ST(#06)
history.undo()  # Back to ST(#05)
assert history.current_state == "ST(#05)"
print(history, end="\n\n")


print("<Test redo()>")
history.redo()  # Back to ST(#06)
history.redo()  # Back to ST(#07)
history.redo()  # Back to ST(#08)
assert history.current_state == "ST(#08)"
print(history, end="\n\n")


print("<Test append() for non-empty REDO stack>")
"""When append() is called for a non-empty REDO stack,
   the History object should clear the REDO stack.
"""
history.append("ST(#11)")
assert history.current_state == "ST(#11)"
assert len(history._stack_redo) == 0
print(history, end='\n\n')


print("<Test clear()>")
history.clear()
assert len(history._stack_undo) == 0
assert len(history._stack_redo) == 0
print(history, end='\n\n')
