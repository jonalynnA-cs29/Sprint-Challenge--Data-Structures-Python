class Node:
    def __init__(self, value=None, next_node=None):
        self.value = value
        self.next_node = next_node

    def get_value(self):
        return self.value

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        self.next_node = new_next


class LinkedList:
    def __init__(self):
        self.head = None

    def add_to_head(self, value):
        node = Node(value)

        if self.head is not None:
            node.set_next(self.head)

        self.head = node

    def contains(self, value):
        if not self.head:
            return False

        current = self.head

        while current:
            if current.get_value() == value:
                return True

            current = current.get_next()

        return False

    def reverse_list(self, node, prev):
        current = self.head  # Start at the head, current
        prev = None  # Starts as None

        while current is not None:  # While the current is not None
            next1 = current.get_next()  # store variable one to the right
            current.set_next(prev)  # change next node of current to previous
            prev = current  # set previous to the current one
            current = next1  # set the current node to the next node
            self.head = prev  # swap """


''' Also with recursion 
        # if self.head is None:
        #     return None
        # elif node.next_node is not None:
        #     new_node = node.get_next()
        #     self.reverse_list(new_node, node)
        # else:
        #     self.head = node

        # node.set_next(prev)
'''
