#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np
import sys

class member(object):
    def __init__(self, mem):
        self.n = mem[0]
        self.a = int(mem[1])
        self.h = int(mem[2])

    def __str__(self):
        return("('{0}', '{1}, '{2}')".format(self.n, self.a, self.h))

class memlist(object):
    def __init__(self, mem_l):
        self.l = []
        for line in mem_l:
            self.l.append(member(line.split(',')))

    def __str__(self):
        tmp = []
        tmp.append([str(mem) for mem in self.l])
        return(str(tmp).strip('[]'))

    def _sorted_l(self):
        return(self.l.sort(key=lambda i: (i.n, i.a, i.h)))



if __name__ == "__main__":
    print("Input member list, end with ctrl-d")
    mem_l = sys.stdin.readlines()
    tmp = memlist(mem_l)
    tmp._sorted_l()
    print(tmp)
