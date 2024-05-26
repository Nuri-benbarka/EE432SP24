class node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data):
        new_node = node(data)
        new_node.next = self.head
        self.head = new_node

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
print(my_list)
print(my_list.search(5))
print(my_list.search("is"))
