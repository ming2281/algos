#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# date:        2019/11/2
# author:      he.zhiming
#

from __future__ import (absolute_import, unicode_literals)

from algos.leetcode.lrucache import LRUCache


def test_lrucache():
    c = LRUCache(2)

    methods = [ "put", "put", "get", "put", "get", "put", "get", "get", "get"]
    args = [ [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]
    for (method_str, arg) in zip(methods, args):
        if method_str == 'put':
            getattr(c, method_str)(arg[0], arg[1])
        if method_str == 'get':
            res = getattr(c, method_str)(arg[0])
            print(res)

    c.print_list()
