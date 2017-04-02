#!/usr/bin/env python3
# coding: utf-8

import xml.etree.ElementTree as ElementTree
import json


def ElementTreeToDict(root):
    if root.getchildren():
        theDict = {root.tag: list(map(ElementTreeToDict, root.getchildren()))}
        theDict.update(('@' + k, v) for k, v in root.attrib.items())
        return theDict
    else:
        return {root.tag: root.text}


def main():
    with open("./books_test.json", "w") as dest_file:
        root = ElementTree.parse('books.xml').getroot()
        theDict = ElementTreeToDict(root)
        theJSON = json.dumps(theDict, indent=2)
        dest_file.write(theJSON)


if __name__ == '__main__':
    main()
