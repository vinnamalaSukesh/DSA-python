class Tree():
    def __init__(self) -> None:
        self.left = None
        self.data = None
        self.right = None

    def add(self,data):
        global root
        child = Tree()
        child.data = data
        if root == None:
            root = child
        else:
            t = root
            while True:
                if(data < root.data):
                    if(t.left == None):
                        t.left = child
                        break
                    t = t.left
                else:
                    if(t.right == None):
                        t.right = child
                        break
                    t = t.right

def print_tree(self):
    if self.left:
        print_tree(self.left)
    print(self.data)
    if self.right:
        print_tree(self.right)

root = None
tree = Tree()
tree.add(5)
tree.add(6)
tree.add(4)
tree.add(7)
tree.add(3)
tree.add(8)
tree.add(2)
tree.add(9)
tree.add(1)
tree.add(10)
tree.add(0)

print_tree(root)
