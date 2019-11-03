#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# date:        2019/10/30
# author:      he.zhiming
#

from __future__ import (absolute_import, unicode_literals)

import heapq
import copy


# CONSTANTS


# PUBLIC APIS
class MinHeap:
    def __init__(self, cap):
        self._cap = cap
        self._h = []
        self._current_size = 0

    def add(self, item):
        if item is None:
            raise ValueError('value can not be None!')

        heapq.heappush(self._h, item)
        self._current_size += 1

        if self._current_size > self._cap:
            heapq.heappop(self._h)

    def pop_top(self):
        if self._h:
            item = heapq.heappop(self._h)

            self._current_size -= 1
            return item
        else:
            raise ValueError('heap is empty')

    def top(self):
        return copy.deepcopy(self._h[0])

    def current_size(self):
        return self._current_size

    def empty(self):
        return self.current_size() == 0

# PRIVATE APIS
