#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np

if __name__ == "__main__":
    l = [int(x)**2 for x in input("Enter a list of numbers: ").split(',') if int(x)%2==1]
    print(l)
