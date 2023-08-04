class Node:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right= None
class BinaryTree:
    def __init__(self):
        self.root=None
    def inorder(self,start):
        if not start:
            return []
        left_side= self.inorder(start.left)
        right_side= self.inorder(start.right)

        return left_side + [start.val] + right_side


if __name__== "__main__":
    tree= BinaryTree()
    tree.root= Node(1)
    tree.root.left= Node(2)
    tree.root.right= Node(3)
    tree.root.left.left= Node(4)
    tree.root.left.right=Node(5)

    print(tree.inorder(tree.root))
