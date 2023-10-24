#!/usr/bin/python3

class Node:
    '''
    This is a class that defines a node of a singly linked list.
    '''
    def __init__(self, data, next_node=None):
        '''
        Initialize Node instance with data and next_node.
        '''
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        '''
        Getter for data.
        '''
        return self.__data

    @data.setter
    def data(self, value):
        '''
        Setter for data.
        '''
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        else:
            self.__data = value

    @property
    def next_node(self):
        '''
        Getter for next_node.
        '''
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        '''
        Setter for next_node.
        '''
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        else:
            self.__next_node = value


class SinglyLinkedList:
    '''
    This is a class that defines a singly linked list.
    '''
    def __init__(self):
        '''
        Initialize SinglyLinkedList instance with head.
        '''
        self.__head = None

    def __str__(self):
        '''
        Returns the entire list in stdout, one node number by line.
        '''
        current = self.__head
        nodes = []

        while current is not None:
            nodes.append(str(current.data))
            current = current.next_node

        return "\n".join(nodes)

    def sorted_insert(self, value):
        '''
        Inserts Node into the correct position in the list (increasin)
        '''

        new_node = Node(value)

        if self.__head is None:
            self.__head = new_node
            return

        if self.__head.data > value:
            new_node.next_node = self.__head
            self.__head = new_node
            return

        current = self.__head

        while current.next_node is not None and current.next_node.data < value:
            current = current.next_node

        new_node.next_node = current.next_node
        current.next_node = new_node
