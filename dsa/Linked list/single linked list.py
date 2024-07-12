head = None
class Node():
    def __init__(self,val) -> None:
        self.data = val
        self.next = None

def append(val):
    global head
    node = Node(val)
    if(head == None):
        head = node
    else:
        t = head
        while(t.next != None):
            t = t.next
        t.next = node

def insert_beginning(val):
    node = Node(val)
    node.next = head
    head = node

def insert_middle(val,pos):
    node = Node(val)
    count = 1
    t = head
    while(count < pos):
        count += 1
        t = t.next
    node.next = t.next
    t.next = node

def delete(val):
    t = head
    flag = 0
    while(t.next.next != None):
        if(t.next.data == val):
            flag = 1
            t.next = t.next.next
            break
        t = t.next
    if(flag == 0):
        print('Element not found')

def display():
    t = head
    while(t != None):
        print(t.data,end='  ')
        t = t.next
    print()
    
#Append to list
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