#linklist
class maku:
    class node:
        def __init__(self, data, next):
            self.data = data
            self.next = next

    def __init__(self):
        self.head = None
        self.size = 0

    def __len__(self):
        return self.size

    def isempty(self):
        return self.size == 0

    def push(self, data):
        self.head = self.node(data, self.head)
        self.size += 1

    def pop(self):
        simpan = self.head.data
        self.head = self.head.next
        self.size -= 1
        return simpan

    def top(self):
        return self.head.data

s = maku()
s.push(1)
print(len(s))
