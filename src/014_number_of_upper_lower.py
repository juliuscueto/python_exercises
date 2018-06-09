#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np

if __name__ == '__main__':
    l = input("Enter a list of words: ")
    upper = sum(c.isupper() for c in l)
    lower = sum(c.islower() for c in l)
    print("UPPER CASE {0}\nLOWER CASE {1}".format(upper, lower))
