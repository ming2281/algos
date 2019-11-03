#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# date:        2019/10/26
# author:      he.zhiming
#

from __future__ import (absolute_import, unicode_literals)

from algos.utils import swap, make_length_list
import attr
import pytest
from pystdutils.assert_uitls import AssertFailedException


@attr.s(slots=True, frozen=False)
class Person(object):
    name = attr.attrib(type=str)


@pytest.mark.parametrize(
    ['arr', 'i', 'j'],

    [
        [None, 0, 0],
        [[1, ], -1, -2]
    ]
)
def test_swap_exc(arr, i, j):
    with pytest.raises((AssertFailedException,)):
        swap(arr, i, j)


def test_swap():
    arr = [1, 2, 3, 4, 5]
    i = 1
    j = 3
    swap(arr, i, j)
    assert arr[i] == 4 and arr[j] == 2

    p1 = Person('name1')
    p2 = Person('name2')
    p3 = Person('name3')
    arr2 = [p1, p2, p3]
    swap(arr2, 0, 2)
    assert arr2[2] == p1 and arr2[0] == p3


def test_make_length_list():
    arr =make_length_list(10)
    assert len(arr) == 10 and arr[9] == None