#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Uebung 2, Aufgabe 2 TEST
# Von Ismail Prada

from Uebung02.Aufgabe02.Aufgabe2_Vorlage import LinkedList


def main():
    pokelist = LinkedList()
    
    print("="*80)
    print("Expected: []\nResult:",pokelist)
    print("="*80)
    
    pokelist.append("Bisasam")
    pokelist.append("Shiggy")
    pokelist.append("Glumanda")
    
    print("Expected: ['Bisasam', 'Shiggy', 'Glumanda']\nResult:\t",pokelist)
    print("="*80)
    
    print("Expected:\nBisasam\nShiggy\nGlumanda")
    print("Result:")
    for node in pokelist:
        print(node)
    print("="*80)
    
    print("Expected:\nGlumanda\nShiggy\nBisasam")
    print("Result:")
    for node in reversed(pokelist):
        print(node)
    print("="*80)
        
    print("Expected: 3\nResult:\t",len(pokelist))
    print("="*80)    
    
    print("Expected: Shiggy\nResult:\t",pokelist[1])
    print("="*80)
    
    print("Expected: True\nResult:\t","Bisasam" in pokelist)
    print("="*80)
    
    print("Expected: False\nResult:\t","Glurak" in pokelist)
    print("="*80)
    
    pokelist[1] = "Shillok"
    print("Expected:  ['Bisasam', 'Shillok', 'Glumanda']\nResult:\t",pokelist)
    print("="*80)
    
    del pokelist[1]
    print("Expected:  ['Bisasam', 'Glumanda']\nResult:\t",pokelist)
    print("="*80)
    
    pokelist.append("Turtok")
    print("Expected:  ['Bisasam', 'Glumanda', 'Turtok']\nResult:\t",pokelist)
    print("="*80)
    
    print("Expected: 2\nResult:\t",pokelist.index("Turtok"))
    print("="*80)
    
    mariolist = LinkedList()
    mariolist.append("Mario")
    mariolist.append("Luigi")
    nintendolist = pokelist + mariolist
    print("Expected:  ['Bisasam', 'Glumanda', 'Turtok', 'Mario', 'Luigi']\nResult:\t",
        nintendolist)
    print("="*80)
    
    mariolist.extend(pokelist)
    print("Expected:  ['Mario', 'Luigi', 'Bisasam', 'Glumanda', 'Turtok']\nResult:\t",
        mariolist)
    print("="*80)
    
    mariolist.clear()
    print("Expected:  []\nResult:\t",mariolist)
    print("="*80)
    
    pokelist.insert(0,"Pikachu")
    print("Expected:  ['Pikachu', 'Bisasam', 'Glumanda', 'Turtok']\nResult:\t",
        pokelist)
    print("="*80)
    
    print("Expected: Pikachu\nResult:\t",
        pokelist.first)
    print("="*80)
    
    print("Expected: Turtok\nResult:\t",
        pokelist.last)
    print("="*80)

    pokelist.insert(pokelist.index("Bisasam"),"Mew")
    print("Expected:  ['Pikachu', 'Mew', 'Bisasam', 'Glumanda', 'Turtok']\nResult:\t",
        pokelist)
    print("="*80)

    print("Expected: Turtok\nResult:\t",
        pokelist[2].next_node.next_node)
    print("="*80)
    
    print("Expected: Bisasam\nResult:\t",
        pokelist[4].previous_node.previous_node)
    print("="*80)
    
    print("Expected: ['Pikachu', 'Mew', 'Bisasam', 'Glumanda', 'Turtok']\nResult:\t",
        list(pokelist))
    print("="*80)
    
    smashlist = ['Samus','Snake','Fox','Kirby']
    pokelist.extend(smashlist)
    print("Expected:   ['Pikachu', 'Mew', 'Bisasam', 'Glumanda', 'Turtok', \
'Samus', 'Snake', 'Fox', 'Kirby']\nResult:\t",
        pokelist)
    print("="*80)
    
    print(repr(pokelist))

if __name__ == '__main__':
    main()
