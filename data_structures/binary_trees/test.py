from node import Node
from binary_tree import BinaryTree

# test case
root = Node(5)
tree = BinaryTree(root)

tree.insert(Node(3))
tree.insert(Node(8))
tree.insert(Node(7))
tree.insert(Node(1))
tree.insert(Node(4))

# print("inorder tree walk recursive:")
# tree.inOrderWalkRecursive(root)
# print("-----------")

# print("inorder tree walk iterative:")
# tree.inOrderWalkIterative(root)
# print("-----------")

print("inorder tree walk Morris:")
tree.inOrderWalkMorris(root)
print("-----------")

# print("Recursive search:")
# recursivelySearchedNode = tree.recursiveSearch(7)
# print("key =", recursivelySearchedNode.key)
# print("-----------")

# print("Iterative search:")
# iterativelySearchedNode = tree.iterativeSearch(7)
# print("key =", recursivelySearchedNode.key)
# print("-----------")

# print("Minimum search:")
# minimum = tree.minimum(root)
# print("key =", minimum.key)
# print("-----------")

# print("Maximum search:")
# maximum = tree.maximum(root)
# print("key =", maximum.key)
# print("-----------")

# print("Successor search:")
# nextNode = tree.successor(iterativelySearchedNode)
# print("key =", nextNode.key)
# print("-----------")

# print("Predecessor search:")
# prevNode = tree.predecessor(iterativelySearchedNode)
# print("key =", prevNode.key)
# print("-----------")

# print("Insert some additional nodes:")
# tree.insert(Node(10))
# tree.insert(Node(9))
# tree.insert(Node(13))
# node10 = tree.iterativeSearch(10)
# print("key =", node10.key)
# print("parent =", node10.parent.key)
# print("-----------")

# print("Deleting")
# node8 = tree.iterativeSearch(8)
# tree.delete(node8)
# print("-----------")