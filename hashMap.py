# def get_hash(key):
#     h = 0
#     for char in key:
    
#         h += ord(char)
#     return h%100



# print(get_hash('March 31'))    


class HashTable:

    # this is without collision ccontrol
    # def __init__(self):
    #     self.max = 10
    #     self.arr = [None for i in range(self.max)]
    
    #with collision handelling
    def __init__(self):
        self.max = 10
        self.arr = [[] for i in range(self.max)] 
    
    
    
    def get_hash(self,key):
        h = 0
        for char in key:
            h += ord(char)

        return h%self.max
    def hash_insertion(self,key,value):
        h = self.get_hash(key)
        self.arr[h].append((key,value))


    def get(self,key):
        h = self.get_hash(key)
        for idx,element in enumerate(self.arr[h]):
            if element[0] == key:
                return element[1]


obj = HashTable()
obj.hash_insertion('September 19',968)
print(obj.get('September 19'))
obj.hash_insertion('March 6',158)
obj.hash_insertion('March 17',412)
print(obj.get('March 6'))
print(obj.arr)
print(obj.get('March 17'))