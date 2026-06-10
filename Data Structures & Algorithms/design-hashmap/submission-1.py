class MyHashMap:

    def __init__(self):
        self.hashmap = []

    def put(self, key: int, value: int) -> None:
        key_exist = False
        for i in range(len(self.hashmap)):
            if self.hashmap[i][0] == key:
                self.hashmap[i][1] = value
                key_exist = True
                break
        if not key_exist:
            self.hashmap.append([key,value])

    def get(self, key: int) -> int:
        for i in range(len(self.hashmap)):
            if self.hashmap[i][0] == key:
                return self.hashmap[i][1]
        return -1

    def remove(self, key: int) -> None:
        for i in range(len(self.hashmap)):
            if self.hashmap[i][0] == key:
                self.hashmap.pop(i)
                break
        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)