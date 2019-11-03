#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# date:        2019/10/27
# author:      he.zhiming
#

from __future__ import (absolute_import, unicode_literals)
import random

# CONSTANTS


# PUBLIC APIS

def get_arr(length, minvalue, maxvalue):
    arr = []
    for _ in range(length):
        arr.append(random.randint(minvalue, maxvalue))

    return arr

# PRIVATE APIS
