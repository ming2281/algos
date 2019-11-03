#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# date:        2019/10/30
# author:      he.zhiming
#

from __future__ import (absolute_import, unicode_literals)

from algos.heap import MinHeap

class Person:
    def __init__(self, name):
        self.name = name
def test_minheap():
    h =MinHeap(3)
    h.add((-1, Person("name1")))
    h.add((0, Person("name0")))
    h.add((4, Person("name4")))
    h.add((3, Person("name3")))

    while not h.empty():
        print(h.pop_top())

