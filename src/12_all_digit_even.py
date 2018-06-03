#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np

def all_even(n):
    while True:
        if (n%10)%2 == 0:
            if n < 10:
                return True
            else:
                n = int(n/10)
        else:
            return False

def all_even_between(start, end, wend=True):
    return np.fromiter((all_even(xi) for xi in np.arange(start, end+wend)), np.bool_)

if __name__ == "__main__":
    start = 1000
    end = 3000
    ret = np.arange(start, end+1)[all_even_between(start, end)]
    print(np.array2string(ret, precision='int', separator=','))
