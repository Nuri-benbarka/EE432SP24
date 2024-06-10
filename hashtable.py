class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

    def __repr__(self):  #HW
        rslt = ""
        rslt += f" ({self.key},{self.value}) "
        current_node = self
        while current_node.next is not None:
            rslt += " --> "
            current_node = current_node.next
            rslt += f" ({current_node.key},{current_node.value}) "
        return rslt


class HashTable:
    def __init__(self, size=10, a=(1 + 5 ** 0.5) / 2):
        self.items = [None for _ in range(size)]
        self.a = a
        self.num_of_items = 0
        self.load_factor = 0
        self.threashold = 0.7

    def rehashing(self):
        old_items = self.items
        self.num_of_items = 0
        self.items = [None for _ in range(len(old_items) * 2)]
        for item in old_items:
            head = item
            while head is not None:
                self.insert(head.key, head.value)
                head = head.next
        self.load_factor = self.num_of_items / len(self.items)


    def hash_function(self, key):
        return int(len(self.items) * ((key * self.a) % 1))

    def hash_function2(self, key):
        key = str(key)
        index = 0
        p = 1
        for c in key:
            index += ord(c) * p
            p *= 37
        return int(len(self.items) * ((index * self.a) % 1))

    def insert(self, key, value):
        index = self.hash_function(key)
        head = self.items[index]
        while head is not None:
            if head.key == key:
                head.value = value
                return
            else:
                head = head.next
        new_node = Node(key, value)
        new_node.next = self.items[index]
        self.items[index] = new_node
        self.num_of_items += 1
        self.load_factor = self.num_of_items / len(self.items)
        if self.load_factor > self.threashold:
            self.rehashing()

    def get(self, key):
        index = self.hash_function(key)
        head = self.items[index]
        while head is not None:
            if head.key == key:
                return head.value
            else:
                head = head.next
        return None

    def delete(self, key):
        index = self.hash_function(key)
        head = self.items[index]
        if head is None:
            return False
        if head.key == key:
            self.items[index] = head.next
            self.num_of_items -= 1
            return True
        while head.next is not None:
            if head.next.key == key:
                head.next = head.next.next
                self.num_of_items -= 1
                return True
            else:
                head = head.next
        return False


my_hash = HashTable(5)
my_hash.insert(22191234, 70)
my_hash.insert(22181234, 75)
my_hash.insert(2200201234, 65)
my_hash.insert(2180201234, 80)
my_hash.insert(2200201234, 85)
my_hash.insert(22191234, 65)
print(my_hash.items)
print(my_hash.num_of_items)
print(my_hash.get(22191234))
print(my_hash.get(22181234))
print(my_hash.get(22181235))
print(my_hash.delete(22191234))
print(my_hash.delete(2180201234))
print(my_hash.delete(22181234))
print(my_hash.delete(22181234))
print(my_hash.items)
