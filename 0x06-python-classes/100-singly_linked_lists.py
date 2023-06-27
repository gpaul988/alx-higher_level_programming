#!/usr/bin/python3
# Graham S. Paul (100-singly_linked_list.py)
"""Explains Classes for singly linked list"""


class Node:
    """
    Shows a node in singly linked list
    """

    def __init__(self, data, next_node=None):
        """Boot Fresh Node"""
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """Acquire Data of node"""
        return self.__data

    @data.setter
    def data(self, value):
        """Calibrate data of node"""
        if type(value) is not int:
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """Acquire next node"""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """calibrate next node"""
        if type(value) is not Node and value is not None:
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """Shows a singly linked list"""

    def __init__(self):
        """Boot fresh singly linked list"""
        self.__head = None

    def __str__(self):
        """Inputs freshh node to singly linked list"""
        string = ""
        temp = self.__head

        while temp is not None:
            string += str(temp.data)
            temp = temp.next_node
            if temp is not None:
                string += "\n"
        return string

    def sorted_insert(self, value):
        """Explain print() representation of singly linked list"""

        new = Node(value)
        if self.__head is None:
            self.__head = new
            return

        temp = self.__head

        if new.data < temp.data:
            new.next_node = self.__head
            self.__head = new
            return

        while temp.next_node is not None and new.data > temp.next_node.data:
            temp = temp.next_node
        new.next_node = temp.next_node
        temp.next_node = new
        return
