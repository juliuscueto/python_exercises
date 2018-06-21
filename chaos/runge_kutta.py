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
    # x0 = 0.09
    # y0 = 0
    # t0 = 0
    # h = 0.01
    # fig, axes = plt.subplots(nrows = 2, ncols = 2)
    # axes[0,0].set_title('X F=0.34875')
    # axes[0,1].set_title('X F=0.42')
    # axes[1,0].set_title('trajectory F=0.34875')
    # axes[1,1].set_title('trajectory F=0.42')
    # vars1 = {"a": -1, "b": 1, "gamma": 0.25, "w": 1, "F":0.34875}
    # vars = {"a": -1, "b": 1, "gamma": 0.25, "w": 1, "F":0.34875}
    # j = 0
    # for vars in [vars1, vars2]:
    #     t = np.arange(0, 200, h)
    #     x = np.zeros_like(t)
    #     y = np.zeros_like(t)
    #     x[0] = x0
    #     y[0] = y0
    #     i = 0
    #     while  i < len(t)-1:
    #         x[i+1], y[i+1] = runge_kutta_2d(duffing_xp, duffing_yp, x[i], y[i], t[i], h, **vars)
    #         i += 1
    #     axes[0,j].plot(t, x)
    #     axes[1,j].scatter(x, y, s=0.01)
    #     j += 1
    # fig.tight_layout()
    # plt.savefig('runge_kutta1.png')
    x0 = 0.09
    y0 = 0
    t0 = 0
    h = 0.01
    # vars = {"a": -1, "b": 1, "gamma": 0.25, "w": 1, "F":0.34875}
    vars = {"a": -1, "b": 1, "gamma": 0.25, "w": 1, "F":0.42}
    for x0 in np.arange(-10,10,1):
        for y0 in np.arange(-10,10,1):
            fig, axes = plt.subplots(nrows = 1, ncols = 2)
            t = np.arange(0, 200, h)
            x = np.zeros_like(t)
            y = np.zeros_like(t)
            x[0] = x0
            y[0] = y0
            i = 0
            while  i < len(t)-1:
                x[i+1], y[i+1] = runge_kutta_2d(duffing_xp, duffing_yp, x[i], y[i], t[i], h, **vars)
                i += 1
            axes[0].plot(t, x)
            axes[1].scatter(x, y, s=0.01)
            axes[0].set_ylim(-1,1)
            axes[1].set_xlim(-2.5,2.5)
            axes[1].set_ylim(-2.5,2.5)
            axes[0].set_title('X x0={0:2.0f} y0={1:2.0f}'.format(x0,y0))
            axes[1].set_title('trajectory x0={0:2.0f} y0={1:2.0f}'.format(x0,y0))
            fig.tight_layout()
            plt.savefig('results/xy0_step_1/x0={0:2.0f}_y0={1:2.0f}.png'.format(x0,y0))
            plt.close()
