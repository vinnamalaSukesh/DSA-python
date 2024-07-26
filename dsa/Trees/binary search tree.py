class Tree():
    def __init__(self) -> None:
        self.left = None
        self.data = None
        self.right = None
def add(data):
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

def delete(data):
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
            add(L[0])
            L.remove(L[0])
            L.sort()
            for i in L:
                add(i)
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
add(5)
add(6)
add(4)
add(7)
add(3)
add(2)
add(8)
add(9)
add(1)
delete(5)
print_tree(root)