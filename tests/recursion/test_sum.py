#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# date:        2019/11/3
# author:      he.zhiming
#

from __future__ import (absolute_import, unicode_literals)

from algos.recursion.sum import get_sum

def test_get_sum():
    assert get_sum(None) == 0
    assert get_sum([]) == 0
    assert get_sum([1, 2, 3, 4]) == 10

    arr = range(100)
    assert get_sum(arr) == sum(arr)


