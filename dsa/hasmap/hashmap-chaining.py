#Time complexity:
#Best case O(1)
# Worst case O(n) when all the keys give same hash value due a bad hash function, then it would be a linear search operation in a a list
#Space complexity Best case O(1) for each key value pair
#Worst case - O(n) - when all keys result same hash value

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
        if(self.arr[h] != []):
            #If already a key value pair exist in that position
            pre = 0
            for i in self.arr[h]:
                if(key in i):
                    pre = 1
                    i[key] = val
            #Check if the key already exists
            #If exists then update the value
            if(pre == 0):
            #If key not exists then
            #Add new key value pair to the same
                self.arr[h].append({key:val})
        else:
            #If the position is empty then simply insert into empty list
            self.arr[h].append({key:val})
    def dis(self,key):
        h = 0
        #To find the value of specific key find the hash value
        for i in key:
            h += ord(i)
        h = h % 100
        #If the position of hash value is empty then element not found
        if(self.arr[h] == []):
            print('Element not found')
        #If not empty search for key in list and print
        for i in self.arr[h]:
            if(key in i):
                print(i[key])
#Create instance
hashmap = HashTable()
#insert
hashmap.add('march 6',0)
hashmap.add('narch 5',1)
hashmap.add('march 7',10)
hashmap.add('march 8',20)
hashmap.add('march 9',30)
hashmap.add('march 10',40)
hashmap.add('march 17',1)
#update
hashmap.add('march 6',1)
#retrive
hashmap.dis('march 6')
hashmap.dis('march 20')
print(hashmap.arr)
