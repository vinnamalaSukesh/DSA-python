class Node():
    def __init__(self,val) -> None:
        self.data = val
        self.next = None

def append(val):
    global head
    node = Node(val)
    if(head == None):
        head = node
        node.next = head
    else:
        t = head
        while(t.next != head):
            t = t.next
        t.next = node
        node.next = head

def insert_beginning(val):
    global head
    node = Node(val)
    node.next = head
    t = head
    while t.next != head:
        t = t.next
    t.next = node
    head = node

def insert_middle(val,pos):
    global head
    node = Node(val)
    count = 1
    t = head
    while(count < pos):
        count += 1
        t = t.next
    node.next = t.next
    t.next = node

def delete(val):
    global head
    t = head
    flag = 0
    while(t.next.next != head):
        if(t.next.data == val):
            flag = 1
            t.next = t.next.next
            break
        t = t.next
    if(flag == 0):
        print('Element not found')

def display():
    global head
    t = head
    while(t.next != head):
        print(t.data,end='  ')
        t = t.next
    print()

head = None
append(2)
append(4)
append(5)
append(5)
append(6)
append(7)
append(8)
append(9)
append(10)
#Insert beginning
insert_beginning(1)
#Insert middle
insert_middle(3,2)
#display the list
display()
#delete a value
delete(5)
display()