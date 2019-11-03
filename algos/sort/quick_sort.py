#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# date:        2019/10/26
# author:      he.zhiming
#

from __future__ import (absolute_import, unicode_literals)

import random

from algos.utils import swap


def quick_sort(arr):
    if not arr or (len(arr) <= 1):
        return arr

    _quick_sort(arr, 0, len(arr) - 1)


def _quick_sort(arr, l, r):
    """排序arr, 区间: [l, r]

    :param arr:
    :param l:
    :param r:
    :return:
    """
    if l >= r:
        return

    random_index = random.randint(l, r)
    swap(arr, l, random_index)

    v = arr[l]
    lt = l
    gt = r + 1
    i = l + 1
    while i < gt:
        if arr[i] < v:
            swap(arr, i, lt + 1)

            i += 1
            lt += 1
        elif arr[i] > v:
            swap(arr, i, gt - 1)
            gt -= 1
        else:
            i += 1

    swap(arr, l, lt)

    _quick_sort(arr, l, lt - 1)
    _quick_sort(arr, gt, r)
