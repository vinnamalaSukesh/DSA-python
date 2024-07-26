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
    t1 = node
    t2 = t1.right
    #t3 = t2.right
    t1.right = t2.left
    t2.left = t1
    t2.parent = t1.parent
    t1.parent = t2

    t1.height = max(cal_height(t1.left),cal_height(t1.right)) + 1
    t2.height = max(cal_height(t2.left),cal_height(t2.right)) + 1

def right_right(node):
    t1 = node
    t2 = t1.left
    #t3 = t2.left
    t1.left = t2.right
    t2.right = t1
    t2.parent = t1.parent
    t1.parent = t2
    t1.height = max(cal_height(t1.left),cal_height(t1.right)) + 1
    t2.height = max(cal_height(t2.left),cal_height(t2.right)) + 1

def left_right(node):
    t1 = node
    t2 = t1.left
    t3 = t2.right

    t1.left = t3
    t2.right = t3.left
    t3.left = t2

    t3.parent = t2.parent
    t2.parent = t3
    if(t2.right):
        t2.right.parent = t2
    t2.height = max(cal_height(t1.left),cal_height(t1.right)) + 1
    t3.height = max(cal_height(t2.left),cal_height(t2.right)) + 1
    t1.height = max(cal_height(t2.left),cal_height(t2.right)) + 1

    t1.left = t3.right
    t3.right = t1
    t3.parent = t1.parent
    if(t1.left):
        t1.left.parent = t1
    t2.height = max(cal_height(t1.left),cal_height(t1.right)) + 1
    t3.height = max(cal_height(t2.left),cal_height(t2.right)) + 1
    t1.height = max(cal_height(t2.left),cal_height(t2.right)) + 1

def right_left(node):
    t1 = node
    t2 = t1.right
    t3 = t2.left

    t1.right = t3
    t2.left = t3.right
    t3.right = t2

    t3.parent = t2.parent
    t2.parent = t3
    if(t2.left):
        t2.left.parent = t2
    t2.height = max(cal_height(t1.left),cal_height(t1.right)) + 1
    t3.height = max(cal_height(t2.left),cal_height(t2.right)) + 1
    t1.height = max(cal_height(t2.left),cal_height(t2.right)) + 1

    t1.right = t3.left
    t3.left = t1
    t3.parent = t1.parent
    if(t1.right):
        t1.right.parent = t1
    t2.height = max(cal_height(t1.left),cal_height(t1.right)) + 1
    t3.height = max(cal_height(t2.left),cal_height(t2.right)) + 1
    t1.height = max(cal_height(t2.left),cal_height(t2.right)) + 1

def check_balance(t):
  if not t:
    return 0  # Handle empty tree case
  lh = check_balance(t.left)
  rh = check_balance(t.right)
  if abs(lh - rh) > 1:
    if lh > rh:
      if t.left.left:
        right_right(t)
      else:
        left_right(t)
    else:
      if t.right.right:
        left_left(t)
      else:
        right_left(t)
  return max(lh, rh) + 1

def elements(node,L):
    if(node.left):
        elements(node.left,L)
    if(node.right):
        elements(node.right,L)
    L.append(node.data)
    return L[:-1]

def print_tree(self):
    if self.left:
        print_tree(self.left)
    print(self.data,self.height)
    if self.right:
        print_tree(self.right)

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