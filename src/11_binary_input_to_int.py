#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np

if __name__ == "__main__":
    l_b = np.array([int(x, 2) for x in input("Enter a list of words: ").split(',')])
    l = np.where(l_b%5==0, 1, 0)
    print(np.array2string(l, precision='int', separator=''))
