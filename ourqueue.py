class OurQueue:
    def __init__(self, capacity):
        self.front = -1
        self.rear = -1
        self.size = 0
        self.capacity = capacity
        self.items = [None for _ in range(capacity)]

    def enqueue(self, data):
        if self.size == self.capacity:
            print("The queue is full")
            return None
        elif self.size == 0:
            self.front = 0
        self.rear += 1
        self.rear %= self.capacity
        self.items[self.rear] = data
        self.size += 1

    def dequeue(self):
        if self.size == 0:
            print("Empty Queue")
            return None
        else:
            data = self.items[self.front]
            self.front += 1
            self.front %= self.capacity
            self.size -= 1
            if self.size == 0:
                self.front = -1
                self.rear = -1
            return data

    def __len__(self):
        return self.size

    def get_front(self):
        if self.size == 0:
            return None
        else:
            return self.items[self.front]


if __name__ == "__main__":
    my_queue = OurQueue(5)
    my_queue.enqueue(1)
    my_queue.enqueue(2)
    my_queue.enqueue(3)
    my_queue.enqueue(4)
    my_queue.enqueue(5)
    my_queue.enqueue(6)
    print(my_queue.dequeue())
    print(my_queue.dequeue())
    print(my_queue.dequeue())
    print(my_queue.dequeue())
    print(my_queue.dequeue())
    print(my_queue.dequeue())
    print(my_queue.get_front())
