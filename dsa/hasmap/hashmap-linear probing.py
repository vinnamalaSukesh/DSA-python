#Time complexity:
class HashTable:
    def __init__(self):
        #Declare an array to store key value pairs
        self.arr = [[] for i in range(100)]

    def add(self,key,val):
        h = 0
        #Find the hash value
        for i in key:
            h += ord(i)
        h = h % 100
        if(self.arr[h] == []):
            self.arr[h] = [key,val]
        else:
            #Check until a empty position found or the key found
            #If already a key value pair exist in that position
            #Check if the key already exists
            #If already exists then update
            #If key not found and empty position found then insert key value pair
            count = 0
            #If the loop iterates more than 100 times then the hashmap is full and no place to insert new val
            while True:
                if(count > 99):
                    break
                if(self.arr[h] == []):
                    self.arr[h] = [key,val]
                    break
                elif(self.arr[h][0] == key):
                    self.arr[h][1] = val
                    break
                else:
                    h += 1
                    h %= 100
                    count += 1

    def dis(self,key):
        h = 0
        #Find the has value for the key
        for i in key:
            h += ord(i)
        h = h % 100
        count = 0
        while True:
            #search for key If before an empty list or the search lasts more than the size of arr
            #then element not found and break
            if(count > 99 or self.arr[h] == []):
                print('Element not found')
                break
            #If the key matches then print the value and break
            if(self.arr[h][0] == key):
                print(self.arr[h])
                break
            count += 1

hashmap = HashTable()
#insert
hashmap.add('march 6',0)
#update
hashmap.add('march 6',1)
hashmap.add('narch 5',1)
hashmap.add('march 7',10)
hashmap.add('march 8',20)
hashmap.add('march 9',30)
hashmap.add('march 10',40)
hashmap.add('march 17',1)
#retrive
hashmap.dis('march 6')
print(hashmap.arr)
