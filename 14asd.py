class HashTable:
    def __init__(self, s):
        self.size = s
        self.slots = [None] * self.size
        self.data = [0] * self.size
        for i in range(self.size):
            self.data[i] = [None]
    def put(self,key,data):
        hashvalue = self.hashfunction(key,len(self.slots))
        self.slots[hashvalue] = key
        if self.data[hashvalue] == [None]:
            self.data[hashvalue].clear()
        self.data[hashvalue].append(data)

    def hashfunction(self,key,size):
        return key%size


    def get(self,key):
        startslot = self.hashfunction(key,len(self.slots))

        data = None
        stop = False
        found = False
        position = startslot
        while self.slots[position] != None and  \
        not found and not stop:
            if self.slots[position] == key:
                found = True
                data = self.data[position]
            else:
                position=self.rehash(position,len(self.slots))
                if position == startslot:
                    stop = True
        return data


#main

a = []

with open('Input.txt','r') as file:
    for line in file:
        for word in line.split():
            a.append(word)

H = HashTable(len(a))

for key in range(len(a)):
    H.put(key, a[key])


f = open('HashTable.txt', 'w')
f.write("========== HashTable ==========\n")
for i in range (len(H.slots)):
    f.write(str(H.slots[i]))
    f.write(": ")
    f.write(str(H.data[i]))
    f.write("\n")
f.close()
