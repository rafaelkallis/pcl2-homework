#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Rafael Kallis


def levenshtein_distance(source, target):
    n = len(source)
    m = len(target)
    d = [[None for _ in range(m + 1)] for _ in range(n + 1)]
    d[0][0] = 0
    for i in range(1, n + 1):
        d[i][0] = d[i - 1][0] + 1
    for j in range(1, m + 1):
        d[0][j] = d[0][j - 1] + 1
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            delete = d[i - 1][j] + 1
            insert = d[i][j - 1] + 1
            substitute = d[i - 1][j - 1] + \
                (1 if source[i - 1] != target[j - 1] else 0)
            d[i][j] = min(
                delete,
                insert,
                substitute
            )

    source_output = []
    target_output = []
    operation_output = []

    i = n
    j = m
    while True:
        if i == 0 or j == 0:
            break
        if d[i - 1][j - 1] < d[i][j]:
            # sub
            source_output.insert(0, source[i - 1])
            target_output.insert(0, target[j - 1])
            operation_output.insert(0, 'S')
            i -= 1
            j -= 1
        elif d[i - 1][j] < d[i][j] and d[i][j - 1] >= d[i][j] and d[i - 1][j - 1] >= d[i][j]:
            # del
            source_output.insert(0, source[i - 1])
            target_output.insert(0, '*')
            operation_output.insert(0, 'D')
            i -= 1
        elif d[i][j - 1] < d[i][j] and d[i - 1][j] >= d[i][j] and d[i - 1][j - 1] >= d[i][j]:
            # ins
            source_output.insert(0, '*')
            target_output.insert(0, target[j - 1])
            operation_output.insert(0, 'I')
            j -= 1
        else:
            source_output.insert(0, source[i - 1])
            target_output.insert(0, target[j - 1])
            operation_output.insert(0, '')
            i -= 1
            j -= 1

    print('\t'.join(source_output))
    print('\t'.join(target_output))
    print('\t'.join(operation_output))
    print('\n')


# Sample Input
inputA1 = ['This', 'is', 'nice', 'cat', 'food', '.']
inputA2 = ['this', 'is', 'the', 'nice', 'cat', '.']
levenshtein_distance(inputA1, inputA2)
"""
prints:

This    is      *       nice    cat     food    .
this    is      the     nice    cat     *       .
S               I                       D
"""

# Input 1
inputB1 = ['The', 'cat', 'likes', 'tasty', 'fish', '.']
inputB2 = ['The', 'cat', 'likes', 'fish', 'very', 'much', '.']
levenshtein_distance(inputB1, inputB2)
"""
prints:

The     cat     likes   *       tasty   fish    .
The     cat     likes   fish    very    much    .
                        I
"""

# Input 2
inputC1 = ['I', 'have', 'adopted', 'cute', 'cats', '.']
inputC2 = ['I', 'have', 'many', 'cats', '.']
levenshtein_distance(inputC1, inputC2)
"""
prints:

I       have    adopted cute    cats    .
I       have    *       many    cats    .
                D
"""
