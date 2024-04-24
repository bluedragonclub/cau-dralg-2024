from singlylinkedlist import Node
from singlylinkedlist import SinglyLinkedList

node = Node()
sll = SinglyLinkedList()

# [Test] Member variables
assert hasattr(node, "_data")
assert hasattr(node, "_next")
assert hasattr(sll, "_head")
assert hasattr(sll, "_tail")
assert hasattr(sll, "_num_nodes")

# [Test] empty() and __len__
assert sll.empty() == True
assert len(sll) == 0

# [Test] Exceptions should be raised for invalid indices.
try:
    sll.insert(1, 'a')
except (ValueError, IndexError) as err:
    #assert str(err) == "Invalid index: 1"
    pass
    
try:
    sll.insert(3, 'garbage')
except (ValueError, IndexError) as err:
    #assert str(err) == "Invalid index: 3"    
    pass

# [Test] Insert a node to the beginning.
alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
for elem in alphabets:
    sll.insert(0, elem)

assert sll.empty() == False
assert str(sll) == "[h]->[g]->[f]->[e]->[d]->[c]->[b]->[a]"
assert len(sll) == len(alphabets)

# [Test] Insert a node to the end.
sll.insert(len(sll), 'x')
sll.insert(len(sll), 'y')
sll.insert(len(sll), 'z')
assert str(sll) == "[h]->[g]->[f]->[e]->[d]->[c]->[b]->[a]->[x]->[y]->[z]"
assert len(sll) == len(alphabets) + 3

# [Test] Insert a node at a specific index.
sll.insert(1, 'A')
assert str(sll) == "[h]->[A]->[g]->[f]->[e]->[d]->[c]->[b]->[a]->[x]->[y]->[z]"
assert len(sll) == len(alphabets) + 4

# [Test] Remove a node at the beginning.
sll.remove(0)
sll.remove(0)
sll.remove(0)
assert str(sll) == "[f]->[e]->[d]->[c]->[b]->[a]->[x]->[y]->[z]"
assert len(sll) == len(alphabets) + 1

# [Test] Remove a node at the end.
sll.remove(len(sll)-1)
assert str(sll) == "[f]->[e]->[d]->[c]->[b]->[a]->[x]->[y]"
assert len(sll) == len(alphabets)

sll.remove(len(sll)-1)
assert str(sll) == "[f]->[e]->[d]->[c]->[b]->[a]->[x]"
assert len(sll) == len(alphabets) - 1

sll.remove(len(sll)-1)
assert str(sll) == "[f]->[e]->[d]->[c]->[b]->[a]"
assert len(sll) == len(alphabets) - 2

# [Test] Remove a node at a specific index.
sll.remove(1)
assert str(sll) == "[f]->[d]->[c]->[b]->[a]"
assert len(sll) == len(alphabets) - 3

sll.remove(2)
assert str(sll) == "[f]->[d]->[b]->[a]"
assert len(sll) == len(alphabets) - 4

sll.remove(1)
assert str(sll) == "[f]->[b]->[a]"
assert len(sll) == len(alphabets) - 5

# [Test] Clear all nodes.
sll.clear()
assert str(sll) == "[]"
assert len(sll) == 0
assert sll.empty()

# [Test] Get a data at a specific index.
for elem in alphabets:
    sll.insert(len(sll), elem)
assert str(sll) == "[a]->[b]->[c]->[d]->[e]->[f]->[g]->[h]"
assert len(sll) == len(alphabets) 

for i, elem in enumerate(alphabets):
    assert elem == sll.get(i)


# [Test] Pop a data at a specific index.
for i, elem in enumerate(alphabets):
    assert elem == sll.pop(0)
    
assert str(sll) == "[]"
assert len(sll) == 0
assert sll.empty()

# [Test] Search a target data.
for elem in alphabets:
    sll.insert(len(sll), elem)
assert str(sll) == "[a]->[b]->[c]->[d]->[e]->[f]->[g]->[h]"
assert len(sll) == len(alphabets) 

for i, elem in enumerate(alphabets):
    data, pos = sll.search(elem)
    assert (elem, i) == (data, pos)
    
for elem in alphabets:
    sll.insert(len(sll), elem)

assert len(sll) == 2*len(alphabets) 

for i, elem in enumerate(alphabets):
    assert elem, len(alphabets)+i == sll.search(elem, i+1)
    

# [Test] Extend a SinglyLinkedList instance with another one.  
sll.clear()
sll2 = SinglyLinkedList()
for elem in alphabets:
    sll.insert(len(sll), elem)
    sll2.insert(len(sll2), elem)

sll.extend(sll2)
assert str(sll) == ("[a]->[b]->[c]->[d]->[e]->[f]->[g]->[h]"\
                    "->[a]->[b]->[c]->[d]->[e]->[f]->[g]->[h]")
assert len(sll) == 2*len(alphabets)


sll.clear()
sll.extend(sll2)
assert str(sll) == ("[a]->[b]->[c]->[d]->[e]->[f]->[g]->[h]")
assert len(sll) == len(alphabets)

sll.clear()
for elem in alphabets:
    sll.insert(len(sll), elem)
    
sll2.clear()
sll.extend(sll2)
assert str(sll) == ("[a]->[b]->[c]->[d]->[e]->[f]->[g]->[h]")
assert len(sll) == len(alphabets)

