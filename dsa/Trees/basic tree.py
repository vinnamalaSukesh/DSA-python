class Tree:
    def __init__(self,data):
        self.data = data
        self.child = []
        self.parent = None
    def add_child(self,child):
        child.parent = self
        self.child.append(child)
    def print_tree(self):
        s = ' ' * get_height(self) + '|--' if(get_height(self) != 0) else ""

        print(s,self.data)
        for i in self.child:
            i.print_tree()

def get_height(node):
    l = 0
    while(node.parent != None):
        l += 1
        node = node.parent
    return l * 5
root = Tree('Electronics')
child1 = Tree("Laptop")
child11 = Tree("asus")
child12 = Tree("hp")
child13 = Tree("mac")
child1.add_child(child11)
child1.add_child(child12)
child1.add_child(child13)

child2 = Tree("mobiles")
child21 = Tree("Mi")
child22 = Tree("samsung")
child23 = Tree("asus")
child2.add_child(child21)
child2.add_child(child22)
child2.add_child(child23)

child3 = Tree("TV")
child31 = Tree("samsung")
child32 = Tree("LG")
child33 = Tree("Sony")
child3.add_child(child31)
child3.add_child(child32)
child3.add_child(child33)

root.add_child(child1)
root.add_child(child2)
root.add_child(child3)
root.print_tree()