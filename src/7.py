#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np

def mul_mat(x, y):
    return np.outer(np.arange(x).T,np.arange(y))

if __name__ == '__main__':
    x, y = [int(n) for n in input("Enter two ints x,y :").split()]
    print(mul_mat(x, y))
