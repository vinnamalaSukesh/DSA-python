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

    def delete(self,data):
        global root
        if(root == None):
            print('Tree is empty')
            return
        else:
            parent = None
            t = root
            found = 0
            while(True):
                if(data == t.data):
                    found = 1
                    break
                elif(data < t.data):
                    parent = t
                    t = t.left
                else:
                    parent = t
                    t = t.right
            if(found == 1):
                L = elements(t,[])
                if(parent == None):
                    root = None
                L.sort()
                l = len(L) // 2
                L = L[l:] + L[:l]
                tree.add(L[0])
                L.remove(L[0])
                L.sort()
                for i in L:
                    tree.add(i)
            else:
                print('Element not found')

def elements(node,L):
    if(node.left):
        elements(node.left,L)
    if(node.right):
        elements(node.right,L)
    L.append(node.data)
    return L[:-1]

def print_tree(self):
    if(self == None):
        return
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
tree.delete(5)
print_tree(root)