#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# date:        2019/10/27
# author:      he.zhiming
#

from __future__ import (absolute_import, unicode_literals)
from algos.sort.merge_sort import merge_sort

from ..common_utils import get_arr


def test_merge_sort():
    arr = get_arr(10, 1, 100)
    print(arr)

    merge_sort(arr)
    print(arr)

