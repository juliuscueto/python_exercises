#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np
import sys

class Robot(object):
    def __init__(self, x0=0, y0=0):
        self.x = x0
        self.y = y0
        self.x0 = x0
        self.y0 = y0

    def _move(self, dir, stp):
        if dir == 'UP':
            self.y += stp
        elif dir == 'DOWN':
            self.y -= stp
        elif dir == 'LEFT':
            self.x -= stp
        elif dir == 'RIGHT':
            self.x += stp
        else:
            print("order must be UP/DOWN/LEFT/RIGHT, ignored order")

    def _accept_cmds(self):
        print("ORDER ME UP/DOWN/LEFT/RIGHT with STEP:")
        cmds = sys.stdin.readlines()
        for cmd in cmds:
            [dir, stp] = cmd.split(' ')
            self._move(dir, int(stp))

    def _print_distance(self):
        return(int(np.rint(np.sqrt((self.x-self.x0)**2 + (self.y - self.y0)**2))))

if __name__ == "__main__":
    rob = Robot()
    rob._accept_cmds()
    print(rob._print_distance())
