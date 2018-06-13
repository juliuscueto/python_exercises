#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np

if __name__ == "__main__":
    ret = 0
    while True:
        line = input("input transaction type and ammount: ")
        if line:
            imput = line.split()
            if imput[0] == "D":
                ret += int(imput[1])
            elif imput[0] == "W":
                ret -= int(imput[1])
            else:
                print("transaction type must be D or W")
        else:
            break
    print(ret)
