#!/usr/bin/env python
# -*- coding: utf-8 -*-

def gen_div7_0to(n):
    for i in range(n+1):
        if i % 7 == 0:
            yield i

if __name__ == "__main__":
    for i in gen_div7_0to(30):
        print(i)
