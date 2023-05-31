#!/usr/bin/python3
"""implementing signly linked list in python"""


class Node:
    """class to define a node in a sinlgly linked list"""

    def __init__(self, data, next_node=None):
        """define data arrtibute of the node
        Args:
            data (int) : data arrtibute of the node
            next_node (Node) : next node of the list
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """get the data of the node"""
        return self.__data

    @data.setter
    def data(self, value):
        """set the value of the data"""
        if not isinstance(value, int):
            raise TypeError("data must be an integer")

        self.__data = value

    @property
    def next_node(self):
        """get the next node"""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """set the next node"""

        if not isinstance(value, Node) and value is not None:
            raise TypeError("next_node must be a Node object")

        self.__next_node = value


class SinglyLinkedList:
    """class to define singly linked list"""

    def __init__(self):
        """initialize head of the singly linked list
        private arrtibute
        """
        self.__head = None

    def sorted_insert(self, value):
        """insert a new node in the singly linked list"""

        node = Node(value)
        if self.__head is None:
            node.next_node = None
            self.__head = node

        elif value < self.__head.data:
            node.next_node = self.__head
            self.__head = node

        else:
            tmp = self.__head
            while (tmp.next_node is not None and value > tmp.next_node.data):
                tmp = tmp.next_node

            node.next_node = tmp.next_node
            tmp.next_node = node

    def __str__(self):
        """define print method of the singly linked list"""
        tmp = self.__head
        while tmp.next_node is not None:
            print(tmp.data)
            tmp = tmp.next_node
        return str(tmp.data)
