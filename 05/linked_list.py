class Node:
    def __init__(self, value: int) -> None:
        self.value = value
        self.next = None


class LinkedList:

    def __init__(self):
        self.head = None

    def find_index_of_value(self, value: int) -> int:

        curr_node = self.head
        curr_index = 0

        while curr_node:
            if curr_node.value == value:
                return curr_index
            curr_node = curr_node.next
            curr_index += 1

        return -1

    def insert_head(self, value: int):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node

    def insert_tail(self, value: int):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node

        curr_node = self.head
        while curr_node.next:
            curr_node = curr_node.next

        curr_node.next = new_node

    def insert_before_value(self, value_node: int, value_comp: int):

        # If the list is empty
        if self.head is None:
            self.insert_head(value_node)
            self.insert_tail(value_comp)
        # Insert new node as head if the value of comparison node is the head
        if self.head.value == value_comp:
            self.insert_head(value_node)
        # Find the indices of the nodes
        node_index = self.find_index_of_value(value_node)
        comp_index = self.find_index_of_value(value_comp)
        # If both nodes don't already exist in the list
        if node_index == -1 and comp_index == -1:
            # Add both nodes in order at the end of the list
            self.insert_head(value_node)
            self.insert_tail(value_comp)


ll = LinkedList()
ll.insert_before_value(47, 53)
ll.insert_before_value(97, 13)
ll.insert_before_value(97, 61)
pass
