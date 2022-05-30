class HMap:
    def __init__(self):
        self.size = 11
        self.index = [[] for i in range(self.size)]

    def hash_f(self, key, size):
        return key % size

    def re_hash_f(self, old_hash, size):
        return (old_hash + 1) % size

    def insert(self, val):
        if val == self.index[self.hash_f(val, self.size)]:
            return
        if self.index[self.hash_f(val, self.size)] == []:
            self.index[self.hash_f(val, self.size)] = val
            return
        if self.index[self.hash_f(val, self.size)] is not []:
            old_hash = self.hash_f(val, self.size)
            while True:
                if self.index[self.re_hash_f(old_hash, self.size)] == []:
                    self.index[self.re_hash_f(old_hash, self.size)] = val
                    return
                old_hash = self.re_hash_f(old_hash, self.size)
        return

    def search(self, val):
        if val == self.index[self.hash_f(val, self.size)]:  # нашли
            return self.hash_f(val, self.size)
        if self.index[self.hash_f(val, self.size)] == []:  # такого нет
            return None
        if self.index[self.hash_f(val, self.size)] is not []:
            old_hash = self.hash_f(val, self.size)
            while True:
                if self.index[self.re_hash_f(old_hash, self.size)] == val:
                    return self.re_hash_f(old_hash, self.size)
                if self.index[self.re_hash_f(old_hash, self.size)] == []:
                    return None
                old_hash = self.re_hash_f(old_hash, self.size)
        return None

    def delete(self, val):
        del self.index[self.search(val)]

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
print(hmap.search(38))
hmap.delete(16)
print("====================")
hmap.print()