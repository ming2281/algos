#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# date:        2019/11/2
# author:      he.zhiming
#

from __future__ import (absolute_import, unicode_literals)

from algos.linkedlist.linkedlist import LinkedList, Node

def print_linkedlist(l: LinkedList):
    if l:
        first = l.head.next_
        while first:
            print(first.value)

            first = first.next_


def test_linkedlist():
    l = LinkedList()
    l.add_first(Node(4))
    l.add_first(Node(3))
    l.add_first(Node(2))

    assert l.contains(4)
    assert l.contains(3)

    assert l.find_node(2) != l.tail
    assert l.head != l.tail
