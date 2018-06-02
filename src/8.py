#!/usr/bin/env python
# -*- coding: utf-8 -*-

if __name__ == "__main__":
    list = input("enter a list of words:").split(",")
    print(sorted(list, key=str.lower))
