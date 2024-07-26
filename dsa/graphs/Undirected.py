edges = [('1','2'),('1','4'),('2','3'),('2','6'),('2','5'),('3','4'),('4','7'),('4','5'),('5','6'),('5','7'),('6','8'),('7','8')]
L = dict()
for edge in edges:
    if(edge[0] not in L.keys()):
        L[edge[0]] = []
    if(edge[1] not in L.keys()):
        L[edge[1]] = []
    L[edge[0]] += [edge[1]]
    L[edge[1]] += [edge[0]]
print(L)





