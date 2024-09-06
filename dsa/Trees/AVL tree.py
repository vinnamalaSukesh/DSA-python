class Tree():
    def __init__(self,data) -> None:
        self.left = None
        self.data = data
        self.right = None
        self.height = 0
        self.parent = None

def add(data):
    global root
    child = Tree(data)
    if(root == None):
        root = child
    else:
        t = root
        while True:
            if(data < root.data):
                if(t.left == None):
                    t.left = child
                    t.left.parent = t
                    set_height(t.left)
                    break
                t = t.left
            else:
                if(t.right == None):
                    t.right = child
                    t.right.parent = t
                    set_height(t.right)
                    break
                t = t.right
    check_balance(root)

def set_height(node):
    while node:
        node.height = max(cal_height(node.left),cal_height(node.right)) + 1
        node = node.parent

def cal_height(node):
    return node.height if node else 0

def left_left(node):
    print('left left',node.data)
    t1 = node
    t2 = t1.right
    t1.right = t2.left
    if t2.left:
        t2.left.parent = t1
    t2.left = t1
    t2.parent = t1.parent
    if t1.parent is None:
        global root
        root = t2
    elif t1 == t1.parent.left:
        t1.parent.left = t2
    else:
        t1.parent.right = t2
    t1.parent = t2
    t1.height = 1 + max(cal_height(t1.left), cal_height(t1.right))
    t2.height = 1 + max(cal_height(t2.left), cal_height(t2.right))

def right_right(node):
    print('right right',node.data)
    t1 = node
    t2 = t1.left
    t1.left = t2.right
    if t2.right:
        t2.right.parent = t1
    t2.right = t1
    t2.parent = t1.parent
    if t1.parent is None:
        global root
        root = t2
    elif t1 == t1.parent.left:
        t1.parent.left = t2
    else:
        t1.parent.right = t2
    t1.parent = t2
    t1.height = 1 + max(cal_height(t1.left), cal_height(t1.right))
    t2.height = 1 + max(cal_height(t2.left), cal_height(t2.right))

def left_right(node):
    #left
    print('left right',node.data)
    t1 = node
    t2 = t1.right
    t3 = t2.left
    t2.left = t3.right
    if t3.right:
        t3.right.parent = t2
    t3.right = t2
    t1.right = t3
    t2.height = 1 + max(cal_height(t2.left), cal_height(t2.right))
    t3.height = 1 + max(cal_height(t3.left), cal_height(t3.right))
    #right
    t3,t2 = t2,t3
    t1 = node
    t2 = t1.left
    t1.left = t2.right
    if t2.right:
        t2.right.parent = t1
    t2.right = t1
    t2.parent = t1.parent
    if t1.parent is None:
        global root
        root = t2
    elif t1 == t1.parent.left:
        t1.parent.left = t2
    else:
        t1.parent.right = t2
    t1.parent = t2
    t1.height = 1 + max(cal_height(t1.left), cal_height(t1.right))
    t2.height = 1 + max(cal_height(t2.left), cal_height(t2.right))
    print_tree(root)
    exit()

def right_left(node):
    pass

def check_balance(node):
    if not node:
        return 0  # Handle empty tree case

    lh = check_balance(node.left)
    rh = check_balance(node.right)

    # Calculate the balance factor
    balance_factor = lh - rh

    # Perform rotations if the node is unbalanced
    if balance_factor > 1:
        if cal_height(node.left.left) >= cal_height(node.left.right):
            right_right(node)  # Left Left Case
        else:
            left_right(node)  # Left Right Case
    elif balance_factor < -1:
        if cal_height(node.right.right) >= cal_height(node.right.left):
            left_left(node)  # Right Right Case
        else:
            right_left(node)  # Right Left Case

    return max(lh, rh) + 1


def elements(node,L):
    if(node.left):
        elements(node.left,L)
    if(node.right):
        elements(node.right,L)
    L.append(node.data)
    return L[:-1]

def print_tree(node):
    if node == None:
       return
    print_tree(node.left)
    print(node.data,node.height)
    print_tree(node.right)

root = None
add(5)
add(6)
add(4)
add(7)
add(3)
add(8)
add(2)
add(9)
add(1)
add(10)
add(0)
print_tree(root)