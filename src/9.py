#!/usr/bin/env python
# -*- coding: utf-8 -*-

if __name__ == '__main__':
    print("Enter Lines till you feel done:")
    lines = []
    while True:
        line = input()
        if line:
            lines.append(line.upper())
        else:
            break
    text = '\n'.join(lines)
    print(text)
