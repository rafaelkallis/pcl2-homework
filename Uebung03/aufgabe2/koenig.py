#!/usr/bin/env python3
# coding: utf-8


def print_list_for_all_letters(word):
    """
    Print a list of all letters from a given string.
    """
    letter_list = [letter for letter in word]
    print("".join(letter_list))


def main():
    '''
    Run as script: print lines of text.
    '''
    print('Make sure to use an utf-8 terminal!')

    print('König')

    print_list_for_all_letters('Überraschung')

    print("{0} means I am super cute.".format(
        "わたしわとても可愛いです。"))

    print('大好')


if __name__ == '__main__':
    main()
