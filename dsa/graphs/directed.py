edges = [('1','2'),('1','4'),('2','3'),('2','6'),('2','5'),('3','4'),('4','7'),('4','5'),('5','6'),('5','7'),('6','8'),('7','8')]
L = dict()
for edge in edges:
    if(edge[0] not in L.keys()):
        L[edge[0]] = []
    if(edge[1] not in L.keys()):
        L[edge[1]] = []
    L[edge[0]] += [edge[1]]

def has_path_DFS(src,des):
    visited = set()
    stack = [src]
    while stack:
        current_node = stack.pop()
        if current_node == des:
            return True
        visited.add(current_node)
        for neighbor in L[current_node]:
            if neighbor not in visited:
                stack.append(neighbor)
    return False

def has_path_BFS(src, des):
    visited = set()
    queue = [src]
    while queue:
        current_node = queue.pop(0)
        if current_node == des:
            return True
        visited.add(current_node)
        for neighbor in L[current_node]:
            if neighbor not in visited:
                queue.append(neighbor)
    return False
#print(has_path_DFS('1','8'))
#print(has_path_BFS('1','8'))