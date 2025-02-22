class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def insert(self, data):
        if self.data is None:
            self.data = data
        elif data < self.data: #Left child
            if self.left is None:
                self.left = Node(data)
            else:
                self.left.insert(data) #recursive call, the self.data will be the left child of the root at every recursive call
        else:  # Right Child
            if self.right is None:
                self.right = Node(data)
            else:
                self.right.insert(data)


                
def inorder(root):
    if root:
        inorder(root.left)
        print(root.data, end=" ")
        inorder(root.right)


root = Node(10)
root.insert(5)
root.insert(15)
root.insert(2)
root.insert(8)
root.insert(12)
root.insert(18)

print("Inorder Traversal (Sorted Order):")
inorder(root)
