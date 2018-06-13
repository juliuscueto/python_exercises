#!/usr/bin/env python
# -*- coding: utf-8 -*-

def validpwd(str):
    if len(str) < 6 or len(str) > 13:
        ret = False
    else:
        f_lwc = False
        f_upc = False
        f_dig = False
        f_chr = False
        for c in str:
            f_lwc = f_lwc or c.islower()
            f_upc = f_upc or c.isupper()
            f_dig = f_dig or c.isdigit()
            f_chr = f_chr or (c=="$") or (c=="#") or (c=="@")
        ret = f_lwc and f_upc and f_dig and f_chr
    return ret

if __name__ == "__main__":
    pwd = [x.lstrip() for x in input("Input comma separated pwds: ").split(',') if validpwd(x.lstrip())]
    print(','.join(pwd))
