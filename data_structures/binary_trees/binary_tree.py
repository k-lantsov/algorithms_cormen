class BinaryTree():
    def __init__(self, root=None):
        self.root = root

    def __str__(self):
        return "Binary tree with root of " + str(self.root)
    
    def inOrderWalkRecursive(self, x):
        if x is not None:
            self.inOrderWalkRecursive(x.left)
            print(x.key)
            self.inOrderWalkRecursive(x.right)

    def inOrderWalkIterative(self, x):
        current = x
        stack = []
        flag = True
        while flag:
            if current is not None:
                stack.append(current)
                current = current.left
            elif stack:
                current = stack.pop()
                print(current.key)
                current = current.right
            else:
                flag = False

    def inOrderWalkMorris(self, x):
        current = x
        while current:
            if current.left is None:
                print(current.key)
                current = current.right
            else:
                # Find the inorder predecessor of current
                prev = current.left
                while prev.right and prev.right != current:
                    prev = prev.right
                # Make current as the right child of its inorder predecessor
                if prev.right is None:
                    prev.right = current
                    current = current.left
                # Revert the changes made to restore the original tree and print current node
                else:
                    prev.right = None
                    print(current.key)
                    current = current.right    
            

    def insert(self, node):
        y = None
        x = self.root
        while x is not None:
            y = x
            if node.key < x.key:
                x = x.left
            else:
                x = x.right
        node.parent = y
        if y is None:
            self.root = node
        elif node.key < y.key:
            y.left = node
        else:
            y.right = node

    def recursiveSearch(self, k, node = None):
        if node is None:
            node = self.root
        if k == node.key:
            return node
        elif k < node.key:
            return self.recursiveSearch(k, node.left)
        else:
            return self.recursiveSearch(k, node.right)

    def iterativeSearch(self, k):
        x = self.root
        while x is not None and k != x.key:
            if k < x.key:
                x = x.left
            else:
                x = x.right
        return x

    def minimum(self, root):
        if root is None:
            return None
        while root.left is not None:
            root = root.left
        return root

    def maximum(self, root):
        if root is None:
            return None
        while root.right is not None:
            root = root.right
        return root

    def successor(self, x):
        if x is None:
            return None
        if x.right is not None:
            return self.minimum(x.right)
        y = x.parent
        while y is not None and x == y.right:
            x = y
            y = y.parent
        return y
    
    def predecessor(self, x):
        if x is None:
            return None
        if x.left is not None:
            return self.maximum(x.left)
        y = x.parent
        while y is not None and x == y.left:
            x = y
            y = y.parent
        return y
    
    def transplant(self, u, v):
        if u.parent is None:
            self.root = v
        elif u.parent.left == u:
            u.parent.left = v
        else:
            u.parent.right = v
        if v is not None:
            v.parent = u.parent
    
    def delete(self, z):
        if z.left is None:
            self.transplant(z, z.right)
        elif z.right is None:
            self.transplant(z, z.left)
        else:
            y = self.minimum(z.right)
            if y.parent != z:
                self.transplant(y, y.right)
                y.right = z.right
                y.right.parent = y
            self.transplant(z, y)
            y.left = z.left
            y.left.parent = y