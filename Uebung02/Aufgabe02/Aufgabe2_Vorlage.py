#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Vorlage
# Uebung 2, Aufgabe 2
# Von Ismail Prada

"""
Feel free to add more attributes and methods if you need them.
You can delete the "raise NotImplementedError"-line whenever 
you finish writing a method. 
Edit the comments of the methods if you want to explain
what you've done.
"""


class Node:
    """Each Node object represents a single node of the linked list
    """
    def __init__(self):
        """No parameter needed in the method itself as attributes are set
        in the LinkedList methods
        """
        self.value = None
        self.next_node = None
        self.previous_node = None
        
    def __str__(self):
        return str(self.value)
        
    def __repr__(self):
        return repr(self.value)


class LinkedList(object):

    def __init__(self):
        self.first = None
        self.last = None
        self.size = 0
        
    def __str__(self):
        nodes = []
        for node in self:
            nodes.append(str(node))
        return "[" + ", ".join(nodes) + "]"
        
    def __repr__(self):
        nodes = []
        for node in self:
            nodes.append(repr(node))
        return "[" + ", ".join(nodes) + "]"
        
    def __len__(self):
        return self.size
        
    def __getitem__(self, index):
        if 0 > index < self.size:
            return None
        idx = 0
        current_node = self.first
        while True:
            if idx == index:
                return current_node
            idx += 1
            current_node = current_node.next_node
        
    def __setitem__(self, index, value):
        if index >= self.size or index < 0:
            return
        idx = 0
        current_node = self.first
        while current_node is not None:
            if idx == index:
                current_node.value = value
                break
            else:
                idx += 1
                current_node = current_node.next_node
        
    def __delitem__(self, index):
        if self.size == 0 or index >= self.size or index < 0:
            return
        current_node = self.first
        idx = 0
        while current_node is not None:
            if idx == index:
                break
            else:
                idx += 1
                current_node = current_node.next_node

        if current_node is None:
            return

        elif self.size == 1:
            self.first = None
            self.last = None

        elif self.size == 2 and self.first == current_node:
            self.last.previous_node = None
            self.first = self.last

        elif self.size == 2 and self.last == current_node:
            self.first.next_node = None
            self.last = self.first

        else:
            current_node.previous_node.next_node = current_node.next_node
            current_node.next_node.previous_node = current_node.previous_node

        self.size -= 1
        del current_node
        
    def __iter__(self):
        current_node = self.first
        while current_node is not None:
            yield current_node
            current_node = current_node.next_node
            
    def __reversed__(self):
        current_node = self.last
        while current_node is not None:
            yield current_node
            current_node = current_node.previous_node
        
    def __contains__(self, value):
        for node in self:
            if value == node.value:
                return True
        return False
        
    def __add__(self, other):
        new_list = LinkedList()
        for node in self:
            new_list.append(node.value)
        for node in other:
            new_list.append(node.value)
        return new_list
        
    def append(self, value):
        self.insert(self.size, value)
    
    def extend(self, other):
        for node_or_value in other:
            self.append(node_or_value if type(node_or_value) != LinkedList else node_or_value.value)
        
    def index(self, value):
        current_node = self.first
        idx = 0
        while current_node is not None:
            if value == current_node.value:
                print(idx)
                return idx
            else:
                idx += 1
                current_node = current_node.next_node

    def insert(self, index, value):
        if 0 < index > self.size:
            return

        new_node = Node()
        new_node.value = value
        new_node.next_node = None
        new_node.previous_node = None

        if self.size == 0:
            self.first = new_node
            self.last = new_node

        elif index == 0:
            self.first.previous_node = new_node
            new_node.next_node = self.first
            self.first = new_node

        elif index == self.size:
            self.last.next_node = new_node
            new_node.previous_node = self.last
            self.last = new_node

        else:
            idx = 1
            current_node = self.first
            while idx < index:
                idx += 1
                current_node = current_node.next_node
            new_node.previous_node = current_node
            new_node.next_node = current_node.next_node
            current_node.next_node.previous_node = new_node
            current_node.next_node = new_node

        self.size += 1
        
    def clear(self):
        for node in self:
            del node
        self.first = None
        self.last = None
        self.size = 0

    def sort(self):
        values = []
        for node in self:
            values.append(node.value)
        self.clear()
        for value in sorted(values):
            self.append(value)
    
def main():
    pass

if __name__ == '__main__':
    main()
