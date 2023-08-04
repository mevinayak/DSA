class Node:
    def __init__(self, val):
        self.val=val
        self.left=None
        self.right=None
class binary_tree:
    def __init__(self):
        self.root= None
    def preorder(self, start, traversal):
        if start is not None:
            traversal+=str(start.val)
            traversal= self.preorder(start.left, traversal)
            traversal= self.preorder(start.right, traversal)
        return traversal


if __name__ == "__main__":
    tree= binary_tree()
    tree.root= Node(1)
    tree.root.left= Node(2)
    tree.root.right= Node(3)
    tree.root.left.left= Node(4)
    tree.root.left.right= Node(5)
    traversal=[]
    print(tree.preorder(tree.root,traversal))

