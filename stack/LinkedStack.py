class Node:
    def __init__(self, elem, link=None):
        self.data = elem
        self.link = link

class LinkedStack:
    def __init__(self):
        self.top = None

    def isEmpty(self):
        return self.top is None

    def push(self, item):
        self.top = Node(item, self.top)

    def peek(self):
        if not self.isEmpty():
            return self.top.data

    def pop(self):
        if not self.isEmpty():
            data = self.top.data
            self.top = self.top.link
            return data

    def size(self):
        node = self.top
        count = 0
        while not node is None:
            node = node.link
            count += 1
        return count

    def __str__(self):
        arr = []
        node = self.top
        while not node is None:
            arr.append(node.data)
            node = node.link
        return str(arr)

