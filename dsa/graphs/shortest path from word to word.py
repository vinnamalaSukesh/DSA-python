start = 'TOON'
target = 'PLEA'
str_list = ['POON','PLEE','SAME','POIE','PLEA','PLIE','POIN']

match = ''
i = 0
steps = [start]
while(start != target):
    if(i < len(str_list)):
        count = 0
        x = list(start)
        y = list(str_list[i])
        for j in range(len(x)):
            if(x[j] != y[j]):
                count += 1
        if(count == 1):
            start = str_list[i]
            if(start == target):
                print('target reached',steps)
                break
            str_list.remove(str_list[i])
            i = 0
            steps.append(start)
        else:
            i += 1
    else:
        print('cannot reach target')
        break