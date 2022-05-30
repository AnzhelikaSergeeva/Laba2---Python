class Node:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Tree:
    def __init__(self):
        self.root = None

    def insert(self, x):
        if self.root is None:
            self.root = Node(x)
            return
        if x < self.root.val:
            if self.root.left is None:
                self.root.left = Tree()
            self.root.left.insert(x)
        else:
            if self.root.right is None:
                self.root.right = Tree()
            self.root.right.insert(x)

    def find(self, x):
        if self.root is None:
            return None
        if self.root.val == x:
            return self.root
        if x < self.root.val:
            if self.root.left is None:
                return None
            return self.root.left.find(x)
        else:
            if self.root.right is None:
                return None
            return self.root.right.find(x)


def heapify(mass):
    mass = set(mass)
    print(mass)

    tree = Tree()
    for i in mass:
        tree.insert(i)

    k = int(input())
    print(tree.find(k))


# t = Tree()
# t.insert(2)
# t.insert(8)
# t.insert(1)
# t.insert(3)
# print(t.find(-1))
# x = 5