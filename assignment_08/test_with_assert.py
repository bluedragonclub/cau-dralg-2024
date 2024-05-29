from binarysearchtree import Node
from binarysearchtree import BinarySearchTree


# [Test] Insert numbers.
bst = BinarySearchTree()
numbers = [6, 3, 2, 4, 5, 8, 10, 9, 11]
for i, elem in enumerate(numbers):
    bst.insert(elem)
    assert len(bst) == (i+1)

assert len(bst) == 9
assert not bst.empty()


# [Test] Traverse the tree.
print("Inorder:", bst.inorder())
print("Preorder:", bst.preorder())
print("Postorder:", bst.postorder())

assert bst.inorder() == [2, 3, 4, 5, 6, 8, 9, 10, 11]
assert bst.preorder() == [6, 3, 2, 4, 5, 8, 10, 9, 11]
assert bst.postorder() == [2, 5, 4, 3, 9, 11, 10, 8, 6]


# [Test] Insert same numbers.
bst = BinarySearchTree()
numbers = [1, 1, 2, 2, 3, 3, 3]
for i, elem in enumerate(numbers):
    bst.insert(elem)
print("Inorder after inserting redundant data", bst.inorder())
    

# [Test] Find the minimum data.
bst.clear()
numbers = [6, 3, 2, 4, 5, 8, 7, 10, 9, 11]
for i, elem in enumerate(numbers):
    bst.insert(elem)
    assert len(bst) == (i+1)
    
    
assert bst.min() == 2
min_node = bst.min(get_node=True)
assert isinstance(min_node, Node)
assert min_node.data == 2

root_subtree = bst.search(data=3)
assert bst.min(root_subtree) == 2
min_node = bst.min(root_subtree, get_node=True)
assert isinstance(min_node, Node)
assert min_node.data == 2

root_subtree = bst.search(data=8)
assert bst.min(root_subtree) == 7
min_node = bst.min(root_subtree, get_node=True)
assert isinstance(min_node, Node)
assert min_node.data == 7


# [Test] Find the maximum data.
assert bst.max() == 11
max_node = bst.max(get_node=True)
assert isinstance(max_node, Node)
assert max_node.data == 11

assert bst.max(bst.search(data=3)) == 5
max_node = bst.max(bst.search(data=3), get_node=True)
assert isinstance(max_node, Node)
assert max_node.data == 5

assert bst.max(bst.search(data=8)) == 11
max_node = bst.max(bst.search(data=8), get_node=True)
assert isinstance(max_node, Node)
assert max_node.data == 11


# [Test] Search a data value in the tree.
for elem in numbers:
    node = bst.search(elem)
    assert node.data == elem
    print("Searh result:", elem, node)


# [Test] Remove a node sequentially
bst = BinarySearchTree()
numbers = [6, 3, 2, 4, 8, 10, 9, 11]
for i, elem in enumerate(numbers):
    bst.insert(elem)
    assert len(bst) == (i+1)

numbers_sorted = sorted(numbers)
for i, elem in enumerate(numbers_sorted):
    node = bst.remove(elem)
    assert node.data == elem
    assert len(bst) == len(numbers) - (i+1)
    assert bst.inorder() == numbers_sorted[i+1:]
    print("Inorder after removing a data:", bst.inorder())


# [Test] Remove a node with a single child (1)
bst.clear()
assert len(bst) == 0
assert bst._root == None

numbers = [6, 3, 2, 4, 8, 10, 9, 11]
for i, elem in enumerate(numbers):
    bst.insert(elem)
    assert len(bst) == (i+1)
    
node = bst.remove(8)
assert node.data == 8
assert len(bst) == len(numbers) - 1
assert bst.inorder() == [2, 3, 4, 6, 9, 10, 11]


# [Test] Remove a node with a single child (2)
bst.clear()
assert len(bst) == 0
assert bst._root == None

numbers = [6, 3, 2, 4, 8, 10, 9, 11]
for i, elem in enumerate(numbers):
    bst.insert(elem)
    assert len(bst) == (i+1)
    
node = bst.remove(4)
assert node.data == 4
assert len(bst) == len(numbers) - 1
assert bst.inorder() == [2, 3, 6, 8, 9, 10, 11]


# [Test] Remove a node with two children (1)
bst.clear()
assert len(bst) == 0
assert bst._root == None

numbers = [6, 3, 2, 4, 8, 7, 10, 9, 11]
for i, elem in enumerate(numbers):
    bst.insert(elem)
    assert len(bst) == (i+1)


node = bst.remove(8)
assert node.data == 8
assert len(bst) == len(numbers) - 1
assert bst.inorder() == [2, 3, 4, 6, 7, 9, 10, 11]
assert bst._root.right.data == 9
assert bst._root.right.left.data == 7
assert bst._root.right.right.data == 10
assert bst._root.right.right.left == None
assert bst._root.right.right.right.data == 11


# [Test] Remove a node with two children (2)
bst.clear()
assert len(bst) == 0
assert bst._root == None

numbers = [6, 4, 2, 5, 1, 3, 8, 7, 10, 9, 11]
for i, elem in enumerate(numbers):
    bst.insert(elem)
    assert len(bst) == (i+1)


node = bst.remove(4)
assert node.data == 4
assert len(bst) == len(numbers) - 1
assert bst.inorder() == [1, 2, 3, 5, 6, 7, 8, 9, 10, 11]
assert bst._root.left.data == 5
assert bst._root.left.left.data == 2
assert bst._root.left.right == None
assert bst._root.left.left.left.data == 1
assert bst._root.left.left.right.data == 3


# [Test] Clear all nodes
bst.clear()
assert len(bst) == 0
assert bst.empty()
assert bst._root == None
