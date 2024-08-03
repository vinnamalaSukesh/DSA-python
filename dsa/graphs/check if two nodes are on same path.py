edges = [('1','2'),('1','4'),('2','3'),('2','6'),('2','5'),('3','4'),('4','7'),('4','5'),('5','6'),('5','7'),('6','8'),('7','8')]
L = dict()
for edge in edges:
    if edge[0] not in L:
        L[edge[0]] = []
    if edge[1] not in L:
        L[edge[1]] = []
    L[edge[0]].append(edge[1])

keys = list(L.keys())
times = dict()
for i in keys:
    times[str(i)] = {'in_time': 0, 'out_time': 0}

def dfs(node, visited, time):
    visited.add(node)
    times[node]['in_time'] = time[0]
    time[0] += 1
    for neighbor in L[node]:
        if neighbor not in visited:
            dfs(neighbor, visited, time)
    times[node]['out_time'] = time[0]
    time[0] += 1

def cal_time():
    visited = set()
    time = [0]
    for key in keys:
        if key not in visited:
            dfs(key, visited, time)

cal_time()

def check(node1,node2):
    if(times[node1]['in_time'] < times[node2]['in_time'] and times[node1]['out_time'] > times[node2]['out_time']):
        print('two nodes in same path')
    elif(times[node2]['in_time'] < times[node1]['in_time'] and times[node2]['out_time'] > times[node1]['out_time']):
        print('two nodes in same path')
    else:
        print('two nodes in different path')

check('6','7')