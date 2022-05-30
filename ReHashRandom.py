class HMap:
    def __init__(self):
        self.size = 11
        self.index = [[] for i in range(self.size)]

    def hash_f(self, key, size):
        return key % size

    def re_hash_f(self, old_hash, size, ri):
        return (old_hash + ri) % size

    def insert(self, val):
        if val == self.index[self.hash_f(val, self.size)]:
            return
        if self.index[self.hash_f(val, self.size)] == []:
            self.index[self.hash_f(val, self.size)] = val
            return
        if self.index[self.hash_f(val, self.size)] is not []:
            old_hash = self.hash_f(val, self.size)
            while True:
                ri = 1
                if self.index[self.re_hash_f(old_hash, self.size, ri)] == []:
                    self.index[self.re_hash_f(old_hash, self.size, ri)] = val
                    return
                ri = (13 * ri + 131) % self.size
                old_hash = self.re_hash_f(old_hash, self.size, ri)
        return

    def search(self, val):
        if val == self.index[self.hash_f(val, self.size)]:
            return self.hash_f(val, self.size)
        if self.index[self.hash_f(val, self.size)] == []:
            return None
        if self.index[self.hash_f(val, self.size)] is not []:
            old_hash = self.hash_f(val, self.size)
            while True:
                ri = 1
                if self.index[self.re_hash_f(old_hash, self.size, ri)] == val:
                    return self.re_hash_f(old_hash, self.size, ri)
                ri = (13 * ri + 131) % self.size
                old_hash = self.re_hash_f(old_hash, self.size, ri)
                if self.index[self.re_hash_f(old_hash, self.size, ri)] == []:
                    return None
        return

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
# hmap.delete(16)
print("====================")
hmap.print()