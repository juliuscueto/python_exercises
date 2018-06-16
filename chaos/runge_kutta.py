#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt

def runge_kutta_2d(fx, fy, x0, y0, t0, h, **kwargs):
        kx1 = fx(x0, y0, t0, **kwargs)
        ky1 = fy(x0, y0, t0, **kwargs)

        kx2 = fx(x0+kx1*h/2, y0+ky1*h/2, t0+h/2, **kwargs)
        ky2 = fy(x0+kx1*h/2, y0+ky1*h/2, t0+h/2, **kwargs)

        kx3 = fx(x0+kx2*h/2, y0+ky2*h/2, t0+h/2, **kwargs)
        ky3 = fy(x0+kx2*h/2, y0+ky2*h/2, t0+h/2, **kwargs)

        kx4 = fx(x0+kx3*h, y0+ky3*h, t0+h, **kwargs)
        ky4 = fy(x0+kx3*h, y0+ky3*h, t0+h, **kwargs)

        x1 = x0 + (kx1 + 2*kx2 + 2*kx3 + kx4)*h/6
        y1 = y0 + (ky1 + 2*ky2 + 2*ky3 + ky4)*h/6

        return x1, y1

def duffing_xp(x, y, t, **kwargs):
    return y

def duffing_yp(x, y, t, **kwargs):
    return -2*kwargs["gamma"]*y - kwargs["a"]*x - kwargs["b"]*x**3 + kwargs["F"]*np.cos(kwargs["w"]*t)

if __name__ == '__main__':
    x0 = 0.09
    y0 = 0
    t0 = 0
    h = 0.01
    vars = {"a": -1, "b": 1, "gamma": 0.25, "w": 1, "F":0.34875}
    t = np.arange(0, 200, h)
    x = np.zeros_like(t)
    y = np.zeros_like(t)
    x[0] = x0
    y[0] = y0
    i = 0
    while  i < len(t)-1:
        x[i+1], y[i+1] = runge_kutta_2d(duffing_xp, duffing_yp, x[i], y[i], t[i], h, **vars)
        i += 1
    plt.plot(x, y)
    plt.show()
