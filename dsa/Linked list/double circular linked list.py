class Node():
    def __init__(self,val) -> None:
        self.left = None
        self.data = val
        self.right = None

def append(val):
    global head,leg
    node = Node(val)
    if(head == None):
        head = node
        leg = node
        node.left = leg
        node.right = head
    else:
        t = head
        while(t.right != head):
            t = t.right
        t.right = node
        node.left = t
        node.right = head
        leg = node
        head.left = leg

def insert_beginning(val):
    global head,leg
    node = Node(val)
    node.left = head.left
    node.right = head
    head.left = node
    head = node
    leg.right = head

def insert_middle(val,pos):
    node = Node(val)
    count = 1
    t = head
    while(count < pos):
        t = t.right
        count += 1
    node.left = t
    node.right = t.right
    t.right.left = node
    t.right = node

def delete(val):
    t = head
    flag = 0
    while(t.right != head):
        if(t.data == val):
            t.left.right = t.right
            t.right.left = t.left
            flag = 1
            break
        t = t.right
    if(flag == 0):
        print('Element not found')

def display():
    t = head
    while(t.right != head):
        print(t.data,end='  ')
        t = t.right
    print(t.data)

head = None
leg = None
append(2)
append(4)
append(5)
append(5)
append(6)
append(7)
append(8)
append(9)
append(10)
insert_beginning(1)
insert_middle(3,2)
delete(5)
display()