class DoublyNode:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

    def __repr__(self):
        return str(self.value)


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def from_array(self, arr):  # without tail
        if self.head is None:
            for a in arr:
                new_node = DoublyNode(a)
                if self.head is None:
                    self.head = new_node
                else:
                    current_node = self.head
                    while current_node.next is not None:
                        current_node = current_node.next
                    current_node.next = new_node
                    new_node.prev = current_node
        else:
            print("Linked list already has nodes")

    def from_array2(self, arr):  # with tail
        if self.head is None:
            for a in arr:
                new_node = DoublyNode(a)
                if self.head is None:
                    self.head = new_node
                    self.tail = new_node
                else:
                    self.tail.next = new_node
                    new_node.prev = self.tail
                    self.tail = new_node
        else:
            print("Linked list already has nodes")

    def __repr__(self):
        output_str = ""
        current_node = self.head
        while current_node is not None:
            # output_str += current_node
            output_str += str(current_node.value)
            output_str += " -> "
            current_node = current_node.next
        return output_str

    def append(self, value):
        new_node = DoublyNode(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node

    def prepend(self, value):
        new_node = DoublyNode(value)
        new_node.next = self.head
        self.head.prev = new_node
        self.head = new_node

    def insert(self, value, pos):
        new_node = DoublyNode(value)
        current_node = self.head
        i = 1
        while i < pos:
            current_node = current_node.next
            i += 1
        new_node.next = current_node.next
        current_node.next = new_node
        new_node.prev = current_node
        new_node.next.prev = new_node

    def pop(self):
        # current_node = self.head
        # while current_node.next != self.tail:
        #     current_node = current_node.next
        # current_node.next = None
        # self.tail = current_node
        self.tail = self.tail.prev
        self.tail.next.prev = None  # for garbage collector
        self.tail.next = None

    def remove(self, pos):
        if pos == 0:
            self.head = self.head.next
        else:
            current_node = self.head
            i = 1
            while i < pos:
                current_node = current_node.next
                i += 1
            current_node.next = current_node.next.next

    def size(self):
        size = 0
        current_node = self.head
        while current_node is not None:
            current_node = current_node.next
            size += 1
        return size

    def search(self, value):
        current_node = self.head
        index = 0
        while current_node is not None:
            if current_node.value == value:
                return index
            else:
                index += 1
                current_node = current_node.next
        return None

    def union(self, llist_2):
        self.tail.next = llist_2.head
        self.tail = llist_2.tail

    def intersection(self, llist2):
        intersec = DoublyLinkedList()
        current_node = self.head
        while current_node:
            if llist2.search(current_node.value) is not None:
                intersec.append(current_node.value)
            current_node = current_node.next
        self.head = intersec.head
        self.tail = intersec.tail

    def swap_nodes(self, position_one, position_two):

        # If both the indices are same
        if position_one == position_two:
            return
        if position_one > position_two:
            position_one, position_two = position_two, position_one

        # Helper references
        one_previous = None
        one_current = None

        two_previous = None
        two_current = None

        current_index = 0
        current_node = self.head

        # LOOP - find out previous and current node at both the positions (indices)
        while current_node is not None:

            # Position_one cannot be equal to position_two,
            # so either one of them might be equal to the current_index
            if current_index == position_one:
                one_current = current_node

            elif current_index == position_two:
                two_current = current_node
                break

            # If neither of the position_one or position_two are equal to the current_index
            if one_current is None:
                one_previous = current_node

            two_previous = current_node

            # increment both the current_index and current_node
            current_node = current_node.next
            current_index += 1

        # Loop ends

        '''SWAPPING LOGIC'''
        # We have identified the two nodes: one_current & two_current to be swapped,
        # Make use of a temporary reference to swap the references
        two_previous.next = one_current
        temp = one_current.next
        one_current.next = two_current.next
        two_current.next = temp

        # if the node at first index is head of the original linked list
        if one_previous is None:
            self.head = two_current
        else:
            one_previous.next = two_current
        # Swapping logic ends

    def skip_i_delete_j(self, i, j):
        if not self.head:
            return
        if i == 0:
            for _ in range(j):
                self.remove(0)
            return

        current = self.head
        count = 1

        while current and count >= 0:
            if count == i:
                for _ in range(j):
                    if current.next:
                        current.next = current.next.next
                        if current.next:
                            current.next.prev = current
                    else:
                        break
                count = -2
            count += 1
            current = current.next


head = DoublyNode(20)
head.next = DoublyNode(4)
head.next.next = DoublyNode(12)

print(head)
print(head.next)
print(head.next.next)
print(" ")


ll = DoublyLinkedList()
ll.from_array2([2, 3, 6, 5, 4])
print(ll)
print(ll)
ll.append(13)
ll.prepend(11)
ll.insert(25, 3)
ll.pop()
ll.remove(1)
ll.remove(2)
print(ll)
print(ll.size())
print(ll.search(5))
print(ll.search(7))

ll2 = DoublyLinkedList()
ll2.append(3)
ll2.append(7)
ll2.append(13)
print(ll2)
print(ll)
ll2.union(ll)
print(ll2)
ll2.intersection(ll)
print(ll2)
ll2.swap_nodes(5, 0)
print(ll2)
ll2.skip_i_delete_j(0, 2)
print(ll2)
ll2.skip_i_delete_j(1, 1)
print(ll2)
