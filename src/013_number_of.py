#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np

if __name__ == '__main__':
    l = input("Enter a list of words: ")
    digits = sum(c.isdigit() for c in l)
    letters   = sum(c.isalpha() for c in l)
    print("LETTERS {0}\nDIGITS {1}".format(letters, digits))
