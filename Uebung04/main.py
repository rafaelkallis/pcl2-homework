#!/usr/bin/env python3
# coding: utf-8

from glob import glob
from lxml import etree
import json
from functools import reduce
import heapq
import bz2
import urllib.request
import random
from tempfile import TemporaryFile


# tested and works!
def getfreqwords(indir, outfile):
    cache = {}
    for file in glob(indir + "/SAC-Jahrbuch_*_mul.xml"):
        tree = etree.parse(file)
        sentences = tree.xpath("//s")
        for sentence in sentences:
            tokens = sentence.xpath("./w/text()")
            if len(tokens) >= 6:
                hash = " ".join(tokens).__hash__()
                if hash in cache:
                    cache[hash] += 1
                else:
                    cache[hash] = 1

    top20hash = set(heapq.nlargest(20, cache, lambda hash: cache[hash]))
    top20sentences = set()

    for file in glob(indir + "/SAC-Jahrbuch_*_mul.xml"):
        tree = etree.parse(file)
        sentences = tree.xpath("//s")
        for sentence in sentences:
            tokens = sentence.xpath("./w/text()")
            if len(tokens) >= 7:
                hash = " ".join(tokens).__hash__()
                if hash in top20hash:
                    top20sentences.add(" ".join(tokens))

    outfile.write('\n'.join(top20sentences))


# not tested! testfile in a+ mode and trainfile in a mode
def gettitles(infile, testfile, trainfile, k):
    # don't know how the file looks, potential wrong read
    tree = etree.iterparse(StringIO(infile))

    # reservoir sampling
    t = 0
    for action, elem in tree:
        if t < k:
            # appends elem to testfile
            testfile.write(elem)
        else:
            m = random.randint(0, t)
            if m < k:
                # temp = testfile;
                # trainfile.append(temp[m]);
                # temp[m] = elem;
                # testfile.clear()
                # testfile = temp
                temp = TemporaryFile("a")

                for idx, line in enumerate(testfile):
                    if m == idx:
                        temp.write(elem)
                        trainfile.write(line)
                    else:
                        temp.write(line)

                # clear testfile
                testfile.seek(0)
                testfile.truncate()

                # testfile = temp
                for line in temp:
                    testfile.write(line)
        t += 1
    return reservoir
