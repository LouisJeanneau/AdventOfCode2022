
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

# double cyclic linked list !!!!!!
class DoubleCyclicLinkedList:
    def __init__(self):
        self.head = None

    def prepend(self, data: list[int, int]):
        new_node = Node(data)
        curr = self.head
        new_node.next = self.head
        self.head.prev = new_node
        new_node.prev = curr.prev
        curr.prev.next = new_node
        self.head = new_node

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

    def prepend_from(self, data: list[int, int], from_node: Node):
        new_node = Node(data)
        curr = from_node.copy()
        new_node.next = from_node
        from_node.prev = new_node
        new_node.prev = curr.prev
        curr.prev.next = new_node

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

    input_list = [[int(i[1])*811589153, i[0]] for i in enumerate(input)]

    dcll = DoubleCyclicLinkedList()
    n = Node(input_list[0])
    dcll.head = n
    dcll.head.next = n
    dcll.head.prev = n
    for inp in input_list[1:]:
        dcll.prepend_from(inp, n)

    l = len(input_list)

    for i in range(10):
        for number in input_list:
            dcll.move(number, number[0] % (l-1))
        print(i)

    head_node = dcll.find_zero()
    sum = 0
    for i in range(3):
        v = dcll.swipe(head_node, (i + 1) * 1000).data[0]
        print(v)
        sum += v
    print(sum)
