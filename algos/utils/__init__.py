#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# date:        2019/10/26
# author:      he.zhiming
#

from __future__ import (absolute_import, unicode_literals)

from typing import Iterable

from pystdutils.assert_uitls import assert_true


# CONSTANTS


# PUBLIC APIS
def swap(arr, i, j):
    """交换数组的两个元素

    [..., i, ..., j, ...]
    [..., j, ..., i, ...]

    :param arr:
    :param i:
    :param j:
    :return:
    """
    assert_true(isinstance(arr, Iterable) and len(arr) > 0 and (0 <= i < len(arr)) and (0 <= j < len(arr)),
                f"arr: {arr}  i: {i} j: {j}")

    arr[i], arr[j] = arr[j], arr[i]

def make_length_list(length, elem=None):
    return [None for _ in range(length)]

# PRIVATE APIS
