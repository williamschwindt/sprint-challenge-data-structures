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
        #handle for empty list
        if not self.head:
            return None

        #handle for 1 el list
        if self.head.next_node is None:
            return self.head

        # > 1 el list
        if node.next_node is not None:
            prev = None
            curr = self.head

            while curr is not None:
                next = curr.next_node
                curr.next_node = prev

                prev = curr
                curr = next
            self.head = prev



        

        
        
