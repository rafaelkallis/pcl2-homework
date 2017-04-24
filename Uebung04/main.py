#!/usr/bin/env python3
# coding: utf-8

from glob import glob
from lxml import etree
import json
from functools import reduce
import heapq


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

    f = open(outfile, 'w')
    f.write('\n'.join(top20sentences))
