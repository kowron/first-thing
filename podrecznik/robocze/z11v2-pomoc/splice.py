#!/usr/bin/env python3
"""Wstawia wnetrza istniejacych rycin (inline SVG) w miejsce znacznikow <!--SVG:id-->.
Uzycie: python3 splice.py robocze/z11-biotechnologia.html   (modyfikuje plik w miejscu)"""
import re, sys, os
D = os.path.dirname(os.path.abspath(__file__))
path = sys.argv[1]
t = open(path, encoding='utf-8').read()
def rep(m):
    f = os.path.join(D, 'svg-%s.html' % m.group(1))
    return open(f, encoding='utf-8').read().rstrip('\n')
t2, n = re.subn(r'[ \t]*<!--SVG:(c11-fig-[a-z]+)-->', rep, t)
open(path, 'w', encoding='utf-8').write(t2)
print('wstawiono', n, 'rycin')
