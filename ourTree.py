class TreeNode:
    def __init__(self, value):
        self.value = value
        self.right = None
        self.left = None


class OurTree:
    def __init__(self, value=None):
        if value is not None:
            self.root = TreeNode(value)
        else:
            self.root = None

    def insert(self, value):
        if self.root is None:
            self.root = TreeNode(value)
        else:
            self._insert(self.root, value)

    def _insert(self, node, value):
        if node is None:
            return TreeNode(value)
        if value > node.value:
            node.right = self._insert(node.right, value)
        if value < node.value:
            node.left = self._insert(node.left, value)
        return node

    def getTreeString(self, node, level, result):
        result += "   " * level + str(node.value) + "\n"
        if node.left is not None:
            result = self.getTreeString(node.left, level + 1, result)
        if node.right is not None:
            result = self.getTreeString(node.right, level + 1, result)
        return result

    def __repr__(self):
        if self.root is None:
            return "empty tree"
        else:
            return self.getTreeString(self.root, 0, "")

    def _search(self, node, value):
        if node is None:
            return None
        elif node.value == value:
            return node.value
        elif value > node.value:
            return self._search(node.right, value)
        elif value < node.value:
            return self._search(node.left, value)

    def search(self, value):
        return self._search(self.root, value)

    def delete(self, value):
        return self._delete(self.root, value)

    def _delete(self, node, value):
        if node is None:
            return None
        elif node.value == value:
            if node.left is None and node.right is None:
                return None
            elif node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            else:
                min_value = self._find_min(node.right)
                node.value = min_value
                self._delete(node.right, min_value)
        elif value > node.value:
            node.right = self._delete(node.right, value)
            return node
        elif value < node.value:
            node.left = self._delete(node.left, value)
            return node

    def _find_min(self, node):
        while node.left is not None:
            node = node.left
        return node.value

    def BFS(self):
        if self.root is None:
            return None
        our_queue = [self.root]
        while len(our_queue) > 0:
            current_node = our_queue.pop(0)
            if current_node.left is not None:
                our_queue.append(current_node.left)
            if current_node.right is not None:
                our_queue.append(current_node.right)
            yield current_node

    def inorder(self, node="root"):
        if node == "root":
            yield from self.inorder(self.root)
        else:
            if node is not None:
                yield from self.inorder(node.left)
                yield node.value
                yield from self.inorder(node.right)

    def preorder(self, node="root"):
        if node == "root":
            yield from self.preorder(self.root)
        else:
            if node is not None:
                yield node.value
                yield from self.preorder(node.left)
                yield from self.preorder(node.right)

    def postorder(self, node="root"):
        if node == "root":
            yield from self.postorder(self.root)
        else:
            if node is not None:
                yield from self.postorder(node.left)
                yield from self.postorder(node.right)
                yield node.value


def our_range(end, start=0, step=1):
    num = start
    while num < end:
        yield num
        num += step


ourtree = OurTree(5)
ourtree.insert(2)
ourtree.insert(7)
ourtree.insert(1)
ourtree.insert(3)
ourtree.insert(4)
ourtree.insert(6)
ourtree.insert(10)
ourtree.insert(11)

print(ourtree)

print(ourtree.search(2))
print(ourtree.search(7))
print(ourtree.search(12))
print(ourtree.search(10))
print(ourtree.search(11))
print(ourtree.search(0))

ourtree.delete(4)
ourtree.delete(10)
ourtree.delete(5)
ourtree.delete(0)
print(ourtree)

ourtree.insert(4)
ourtree.insert(12)
ourtree.insert(0)
ourtree.insert(5)
print(ourtree)

for i in our_range(10):
    print(i, end=" ")
print(" ")
print("BFS:")
for node in ourtree.BFS():
    print(node.value, end=" ")
print(" ")
print("inorder:")
for node in ourtree.inorder():
    print(node, end=" ")
print(" ")
print("preorder:")
for node in ourtree.preorder():
    print(node, end=" ")
print(" ")
print("postorder:")
for node in ourtree.postorder():
    print(node, end=" ")
