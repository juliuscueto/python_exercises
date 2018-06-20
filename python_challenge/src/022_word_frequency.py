#!/usr/bin/env python
# -*- coding: utf-8 -*-

from collections import Counter

if __name__ == "__main__":
    tmp = input("type whatever you want, in one line:\n")
    c = Counter(tmp.split(' '))
    for key in c:
        print("{0}:{1}".format(key, c[key]))
