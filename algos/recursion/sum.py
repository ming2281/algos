#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# date:        2019/11/3
# author:      he.zhiming
#

from __future__ import (absolute_import, unicode_literals)

def _get_sum(arr, l, r):
    """
    [l, r]

    :param arr:
    :param l:
    :param r:
    :return:
    """
    if l == r:
        return arr[l]
    if l > r:
        return 0

    return arr[l] + _get_sum(arr, l+1, r)

def get_sum(arr):
    if not arr:
        return 0
    if len(arr) == 1:
        return arr[0]

    return _get_sum(arr, 0, len(arr) -1)