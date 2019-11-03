#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# date:        2019/10/26
# author:      he.zhiming
#

from __future__ import (absolute_import, unicode_literals)

from algos.sort.quick_sort import quick_sort
import random
from pyloggers import CONSOLE


def get_arr(length, minvalue, maxvalue):
    arr = []
    for _ in range(length):
        arr.append(random.randint(minvalue, maxvalue))

    return arr


def test_quick_sort():
    N = 10000000
    arr = get_arr(N, 1, 100)
    CONSOLE.info('start')
    # quick_sort(arr)
    CONSOLE.info('end')

    CONSOLE.info('start')
    arr.sort()
    CONSOLE.info('end')

