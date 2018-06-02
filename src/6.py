#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np

def q(d, c = 50, h = 30):
    return np.sqrt(np.multiply(d, 2*c)/h)

if __name__ == "__main__":
    n = [float(x) for x in input("enter a list of numbers:").split()]
    print(q(np.array(n)).astype(int))
