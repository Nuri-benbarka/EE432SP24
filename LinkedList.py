class node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert(self, data, index=0):
        new_node = node(data)
        current_node = self.head
        if current_node is None:
            self.head = new_node
            self.tail = new_node
        elif index == 0:
            new_node.next = self.head
            self.head = new_node
        else:
            i = 0
            while i < index - 1 and current_node.next is not None:
                current_node = current_node.next
                i += 1
            new_node.next = current_node.next  # 4 -> 5
            current_node.next = new_node  # 3 -> 4
        if current_node == self.tail:
            self.tail = new_node

    def append(self, data):
        newNode = node(data)
        if self.head is not None:
            self.tail.next = newNode
            self.tail = newNode
        else:
            self.head = newNode
            self.tail = newNode

    def search(self, data):
        current_node = self.head
        current_index = 0
        while current_node is not None:
            if current_node.data == data:
                return current_index
            else:
                current_node = current_node.next
                current_index += 1
        return None

    def __str__(self):
        result = ""
        current_node = self.head
        while current_node is not None:
            result = str(current_node.data) + result
            result = " -> " + result
            current_node = current_node.next
        return result


my_node1 = node("My")
my_node2 = node("name")
my_node3 = node(5)
my_node1.next = my_node2
my_node2.next = my_node3
print(my_node1.next)
print(my_node2)
print(my_node1.next.next.data)
my_list = LinkedList()
my_list.insert("My")
my_list.insert("name")
my_list.insert("is")
my_list.insert("Nuri")
print(my_list.tail.data)
my_list.insert(5, 0)
print(my_list.tail.data)
print(my_list)
print(my_list.search(5))
print(my_list.search("is"))

