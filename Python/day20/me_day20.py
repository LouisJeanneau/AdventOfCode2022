# ChatGPT generated double cyclic linked list !!!!!!
import numpy


class Node:
    def __init__(self, data: list[int, int]):
        self.data = data
        self.next = None
        self.prev = None

    def copy(self):
        new_node = Node(self.data.copy())
        new_node.next = self.next
        new_node.prev = self.prev
        return new_node


class DoubleCyclicLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data: list[int, int]):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            new_node.next = self.head
            new_node.prev = self.head
        else:
            curr = self.head
            while curr.next != self.head:
                curr = curr.next
            curr.next = new_node
            new_node.prev = curr
            new_node.next = self.head
            self.head.prev = new_node

    def prepend(self, data: list[int, int]):
        new_node = Node(data)
        curr = self.head
        new_node.next = self.head
        self.head.prev = new_node
        new_node.prev = curr.prev
        curr.prev.next = new_node
        self.head = new_node

    def delete(self, data: list[int, int]):
        if self.head is None:
            return
        if self.head.next == self.head:
            if self.head.data == data:
                self.head = None
            return
        curr = self.head
        while curr.next != self.head:
            if curr.data == data:
                break
            curr = curr.next
        if curr.data == data:
            curr.prev.next = curr.next
            curr.next.prev = curr.prev
            if curr == self.head:
                self.head = curr.next
        else:
            print(f"{data} not found in the list")

    def print_list(self):
        curr = self.head
        while curr:
            # print(str(curr.data[0]) + ":" + str(curr.data[1]), sep=' ', end=",    ")
            print(str(curr.data[0]), sep='', end=", ")
            curr = curr.next
            if curr.data == self.head.data:
                break
        print()

    # Homemade addition
    def swipe(self, from_node: Node, position: int) -> Node:
        curr = from_node
        if numpy.sign(position) == 1:
            for _ in range(0, abs(position)):
                curr = curr.next
        elif numpy.sign(position) == -1:
            for _ in range(0, abs(position)):
                curr = curr.prev
        return curr

    def append_from(self, data: list[int, int], from_node: Node):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            new_node.next = self.head
            new_node.prev = self.head
        else:
            curr = from_node.copy()
            from_node.next = new_node
            new_node.prev = from_node
            new_node.next = curr.next
            curr.next.prev = new_node

    def prepend_from(self, data: list[int, int], from_node: Node):
        new_node = Node(data)
        curr = from_node.copy()
        new_node.next = from_node
        from_node.prev = new_node
        new_node.prev = curr.prev
        curr.prev.next = new_node

    def move_head(self, to_node):
        self.head = to_node

    def find_node(self, data):
        curr = self.head
        while curr.data != data:
            curr = curr.next
        return curr

    def find_zero(self):
        curr = self.head
        while curr.data[0] != 0:
            curr = curr.next
        return curr

    def move(self, data, position):
        if not position:
            return
        curr = self.find_node(data)
        prev_node = curr.prev
        next_node = curr.next
        for _ in range(position):
            curr = curr.next
        prev_node.next = next_node
        next_node.prev = prev_node
        n = Node(data)
        curr.next.prev = n
        n.next = curr.next
        n.prev = curr
        curr.next = n
        if data == self.head.data:
            self.head = curr.prev


with open("input.txt") as f:
    input = f.read().splitlines()
    # Parse cost
    input_list = [[int(i[1]), i[0]] for i in enumerate(input)]

    dcll = DoubleCyclicLinkedList()
    dcll.append(input_list[0])
    starting_node = dcll.head
    for inp in input_list[1:]:
        dcll.prepend_from(inp, starting_node)
    dcll.print_list()
    l = len(input_list)

    for number in input_list:
        dcll.move(number, number[0] % (l-1))
        # dcll.print_list()
        '''
        node = dcll.find_node(number)
        if number[0]:
            dcll.delete(number)

        if numpy.sign(number[0]) == 1:
            from_node = dcll.swipe(node, number[0] % (len(input_list)))
            dcll.append_from(number, from_node)
        elif numpy.sign(number[0]) == -1:
            from_node = dcll.swipe(node, number[0] )
            dcll.prepend_from(number, from_node)
        '''

    dcll.print_list()

    head_node = dcll.find_zero()
    sum = 0
    for i in range(3):
        v = dcll.swipe(head_node, (i + 1) * 1000).data[0]
        print(v)
        sum += v
    print(sum)
