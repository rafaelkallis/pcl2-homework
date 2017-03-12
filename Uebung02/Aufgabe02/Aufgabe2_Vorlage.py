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
        ##TODO
		raise NotImplementedError
        
    def __repr__(self):
        ##TODO
		raise NotImplementedError


class LinkedList(object):
    """This is a doubly linked List. Each node know only its neighbors.
    """
    def __init__(self):
        self.first = None #the first node: Don't forget to update!
        self.last = None #the last node: Don't forget to update!
        # More needed?
        
    def __str__(self):
        """Used by the print-function."""
        ##TODO
		raise NotImplementedError
        
    def __repr__(self):
        """Sets the representation of the object.
        """
        ##TODO
		raise NotImplementedError
        
    def __len__(self):
        """Returns number of nodes"""
        ##TODO
		raise NotImplementedError
        
    def __getitem__(self, key):
        """Returns value of a node in a certain position"""
        ##TODO
		raise NotImplementedError
        
    def __setitem__(self, key, value):
        """Assigns a new value to a node in a certain position"""
        ##TODO
		raise NotImplementedError
        
    def __delitem__(self, key):
        """Deletes a node in a certain position"""
        ##TODO
		raise NotImplementedError
        
    def __iter__(self):
        """Makes iteration of the linked list possible.
        Should yield content (aka value) of the nodes.
        """
        ##TODO
		raise NotImplementedError
            
    def __reversed__(self):
        """Like iter, but in reverse.
        Should yield content (aka value) of the nodes."""
        ##TODO
		raise NotImplementedError
        
    def __contains__(self, item):
        """Checks if a value is in the linked list."""
        ##TODO
		raise NotImplementedError
        
    def __add__(self, other):
        """Concatenates two linked lists and returns the new one."""
        ##TODO
		raise NotImplementedError
        
    def append(self, value):
        """Adds a new node to the list and assigns it a given value."""
        ##TODO
		raise NotImplementedError
    
    def extend(self, other):
        """Extends one linked list with another linked list or an array.
        """
        ##TODO
		raise NotImplementedError
        
    def index(self,item):
        """Returns first index in which a given value is found."""
        ##TODO
		raise NotImplementedError
        
    def insert(self, key, value):
        """Inserts a value in a given position"""
        ##TODO
		raise NotImplementedError
        
    def clear(self):
        """Empties the linked list."""
        ##TODO
		raise NotImplementedError
        
    # Some private methods needed?
    
def main():
    pass

if __name__ == '__main__':
    main()
