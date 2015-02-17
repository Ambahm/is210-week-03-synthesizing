#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Contains expectations."""


import inquisition

# from inquisition import SPANISH
FILE = inquisition.SPANISH

WO_REP = 'Spanish'  # first instance of Spanish to be removed at index 0
WO_LEN = len(WO_REP)  # lenght of word to be removed
FLEMISH = FILE[0:FILE.index(WO_REP)]+'Flemish'+FILE[FILE.index(WO_REP)+WO_LEN:]
print "\n", FLEMISH
