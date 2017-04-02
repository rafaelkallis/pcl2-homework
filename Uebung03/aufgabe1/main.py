#!/usr/bin/env python3
# coding: utf-8


def printBin(filename):
    pentadCount = 0
    currentBinPentad = []
    currentCharPentad = []

    with open(filename, "r") as f:
        byte = f.read(1)
        while byte != "":
            currentBinPentad.append(str(bin(ord(byte))) + " ")
            currentCharPentad.append(str(byte))

            byte = f.read(1)
            pentadCount += 1

            if pentadCount == 5:
                print("\t".join(currentBinPentad), "\t|" +
                      "".join(currentCharPentad) + "|")
                currentBinPentad = []
                currentCharPentad = []
                pentadCount = 0
