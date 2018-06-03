#!/usr/bin/env python
# -*- coding: utf-8 -*-

if __name__ == "__main__":
    l = input("Enter a number: ")
    if l.isdigit():
        size = len(l)
        num = int(l)
        ret = (10**(3*size)+2*10**(2*size)+3*10**(size)+4)*num
        print(ret)
    else:
        print("Input must only contain digits")
