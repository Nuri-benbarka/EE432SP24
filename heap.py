class Ourheap:
    def __init__(self, capacity):
        self.tree = [None] * capacity  # Initialize an array to store the BST nodes
        self.capacity = capacity
        self.last_node_index = 0

    def insert(self, key):
        if self.last_node_index > self.capacity:
            print("Heap is full")
        else:
            self.tree[self.last_node_index] = key
            i = self.last_node_index
            self.last_node_index += 1
            while i > 0:
                if i % 2 == 0:
                    if self.tree[i] > self.tree[(i - 2) // 2]:
                        self.tree[i], self.tree[(i - 2) // 2] = self.tree[(i - 2) // 2], self.tree[i]
                        i = (i - 2) // 2
                    else:
                        break
                if i % 2 == 1:
                    if self.tree[i] > self.tree[(i - 1) // 2]:
                        self.tree[i], self.tree[(i - 1) // 2] = self.tree[(i - 1) // 2], self.tree[i]
                        i = (i - 1) // 2
                    else:
                        break

    def delete(self):
        if self.last_node_index == 0:
            print("empty tree")
            return
        item = self.tree[0]
        self.tree[0], self.tree[self.last_node_index - 1] = self.tree[self.last_node_index - 1], self.tree[0]
        self.tree[self.last_node_index - 1] = None
        self.last_node_index -= 1
        i = 0
        while i < self.last_node_index:
            if 2 * i + 1 < self.last_node_index and 2 * i + 2 < self.last_node_index:
                if self.tree[2 * i + 2] < self.tree[2 * i + 1]:
                    swap = 2 * i + 1
                else:
                    swap = 2 * i + 2
                if self.tree[i] < self.tree[swap]:
                    self.tree[i], self.tree[swap] = self.tree[swap], self.tree[i]
                else:
                    break
            elif 2 * i + 1 < self.last_node_index and self.tree[i] < self.tree[2 * i + 1]:
                self.tree[i], self.tree[2 * i + 1] = self.tree[2 * i + 1], self.tree[i]
                i = 2 * i + 1
                continue
            elif 2 * i + 2 < self.last_node_index and self.tree[i] < self.tree[2 * i + 2]:
                self.tree[i], self.tree[2 * i + 2] = self.tree[2 * i + 2], self.tree[i]
                i = 2 * i + 2
                continue
            else:
                break
        return item

    def __repr__(self):
        if not any(self.tree):
            return '<empty tree>'
        return '\n'.join(self._build_tree_string(0, 0))

    def _build_tree_string(self, index, depth):
        result = []
        if index < self.capacity and self.tree[index] is not None:
            node_repr = f"{' ' * (depth * 2)}[{index}]: {self.tree[index]}"
            result.append(node_repr)
            result.extend(self._build_tree_string(2 * index + 1, depth + 1))
            result.extend(self._build_tree_string(2 * index + 2, depth + 1))
        return result


# Example usage
if __name__ == "__main__":
    bst = Ourheap(15)  # Array-based BST with capacity for 15 nodes
    bst.insert(50)
    bst.insert(30)
    bst.insert(20)
    bst.insert(40)
    bst.insert(70)
    bst.insert(60)
    bst.insert(80)

    print("BST Representation:\n", bst)

    print(bst.delete())
    print(bst.delete())
    print(bst.delete())
    print(bst.delete())
    print(bst.delete())
    print(bst.delete())
