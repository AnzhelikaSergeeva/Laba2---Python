class HMap:
    def __init__(self):
        self.size = 11
        self.index = [[] for i in range(self.size)]

    def hash_f(self, key, size):
        return key % size

    def insert(self, val):
        self.index[self.hash_f(val, self.size)].append(val)
        return

    def search(self, val):
        for i in range(len(self.index[self.hash_f(val, self.size)])):
            if self.index[self.hash_f(val, self.size)][i] == val:
                return i
        return None

    def delete(self, val):
        for i in range(len(self.index[self.hash_f(val, self.size)])):
            if self.index[self.hash_f(val, self.size)][i] == val:
                self.index[self.hash_f(val, self.size)][:] = self.index[self.hash_f(val, self.size)][:i] + self.index[self.hash_f(val, self.size)][i+1:]
                return self.index[self.hash_f(val, self.size)]

    def print(self):
        for i in self.index:
            print(i)


hmap = HMap()
hmap.insert(5)
hmap.insert(16)
hmap.insert(7)
hmap.insert(27)
hmap.insert(38)
hmap.insert(8)
print(hmap.search(7))
hmap.delete(16)
print("====================")
hmap.print()