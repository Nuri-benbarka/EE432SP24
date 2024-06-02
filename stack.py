class DoublyNode:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class StackLL:
    def __init__(self):
        self.head = None
        self.tail = None
        self.len = 0

    def push(self, item):
        newNode = DoublyNode(item)
        self.len += 1
        if self.head is None:
            self.head = newNode
            self.tail = newNode
        else:
            self.tail.next = newNode
            newNode.prev = self.tail
            self.tail = newNode

    def pop(self):
        if self.tail is None:
            return "Stack underflow"
        elif self.tail == self.head:
            data = self.tail.data
            self.head = None
            self.tail = None
            self.len -= 1
            return data
        else:
            data = self.tail.data  #1
            self.tail.prev.next = None  #2
            self.tail = self.tail.prev  #3
            self.len -= 1
            return data

    def top(self):
        return self.tail.data

    def __len__(self):
        return self.len


class StackArr:
    def __init__(self, capasity):
        self.items = [None for _ in range(capasity)]
        self.top = -1

    def push(self, data):
        if self.top == len(self.items)-1:
            print("Stack overflow")
        else:
            self.top += 1
            self.items[self.top] = data

    def pop(self):
        if self.top == -1:
            return  "Stack underflow"
        else:
            data = self.items[self.top]
            self.top -= 1
            return data

    def __len__(self):
        return self.top + 1

    def top(self):
        return self.items[self.top]


mystack1 = StackLL()
mystack1.push(10)
mystack1.push(20)
mystack1.push(30)
print(len(mystack1))
print(mystack1.pop())
print(mystack1.pop())
print(mystack1.pop())
print(mystack1.pop())
print(len(mystack1))
print(mystack1)

print(" ")
print("stack array")
mystack = StackArr(2)
mystack.push(10)
mystack.push(20)
mystack.push(30)
print(len(mystack))
print(mystack.pop())
print(mystack.pop())
print(mystack.pop())
print(mystack.pop())
print(len(mystack))
print(mystack)
