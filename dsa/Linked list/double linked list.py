class Node():
    #Blue print for node
    def __init__(self,val) -> None:
        self.left = None #left pointer
        self.data = val  #data
        self.right = None #right pointer

def append(val):
    global head,leg #make head and leg variables accessible in this function
    node = Node(val) #Initialize node
    if(head == None): # If head equal to none then head = node
        head = node
        leg = node
        node.left = leg #pointing to same node
        node.right = head
    else:
        t = head #pointer to traverse list
        while(t.right != head):
            t = t.right
        t.right = node #set before node right pointer to node
        node.left = t
        leg = node
        node.right = head
        head.left = node

def insert_beginning(val):
    global head,leg
    node = Node(val)
    node.right = head
    node.left = leg
    leg.right = node
    head.left = node
    head = node

def insert_middle(val,pos):
    node = Node(val)
    t = head
    count = 1
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
    while(t.right != None):
        if(t.data == val):
            t.left.right = t.right
            t.right.left = t.left
            flag = 1
            break
        t = t.right
    if(flag == 0):
        print('Element not found')

def display():
    global head
    t = head
    while(t.right != head):
        print(t.data,end = '  ')
        t = t.right
    print(t.data)

def display_reverse():
    global leg
    t = leg
    while(t != head):
        print(t.data,end = '  ')
        t = t.left
    print(t.data)
#Initializing head pointer
head = None
#Initializing end pointer
leg = None
#Appending elements to list
append(2)
append(4)
append(5)
append(5)
append(6)
append(7)
append(8)
append(9)
append(10)
#Insert at beginning
insert_beginning(1)
#Insert at middle
insert_middle(3,2)
#delete elements
delete(5)
#display list
display()
display_reverse()