#!/usr/bin/python3
"""
This module defines a Node class and a SinglyLinkedList class.
"""


class Node:
    """
    This class defines a node of a singly linked list by data and next_node.
    """

    def __init__(self, data, next_node=None):
        """
        This method initializes the node.
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """
        This method retrieves the data of the node.
        """
        return self.__data

    @data.setter
    def data(self, value):
        """
        This method sets the data of the node.
        """
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """
        This method retrieves the next node of the node.
        """
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """
        This method sets the next node of the node.
        """
        if not isinstance(value, Node) and value is not None:
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """
    This class defines a singly linked list by head.
    """

    def __init__(self):
        """
        This method initializes the singly linked list.
        """
        self.__head = None

    def __str__(self):
        """
        Method returns the string representation of the singly linked list.
        """
        result = ""
        current = self.__head
        while current:
            result += str(current.data) + "\n"
            current = current.next_node
        return result[:-1]

    def sorted_insert(self, value):
        """
        Inserts new node into the correct sorted position in the list.
        """
        new_node = Node(value)

        if not self.__head or value < self.__head.data:
            new_node.next_node = self.__head
            self.__head = new_node
            return

        current = self.__head

        while current.next_node and value > current.next_node.data:
            current = current.next_node

        new_node.next_node = current.next_node
        current.next_node = new_node
