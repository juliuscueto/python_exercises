#!/usr/bin/env python
# -*- coding: utf-8 -*-

if __name__ == "__main__":
    list = [word.lower() for word in input("Enter a list of words: ").split()]
    print(sorted(set(list)))
