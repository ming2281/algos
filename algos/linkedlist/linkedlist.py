#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# date:        2019/11/2
# author:      he.zhiming
#

from __future__ import (absolute_import, unicode_literals)


class Node:
    def __init__(self, value, prev=None, next_=None):
        """
        :param T value:
        :param Node prev:
        :param Node next_:
        """
        self.value = value
        self.prev = prev
        self.next_ = next_


class LinkedList:
    def __init__(self):
        """
        搞两个dummy节点
        """
        self.head = Node(None)
        self.tail = Node(None)
        self.head.prev = None
        self.head.next_ = self.tail
        self.tail.next_ = None
        self.tail.prev = self.tail

        self.size = 0

    def remove_node(self, node: Node):
        """

        :param node:
        :return:
        """
        if not node:
            return

        nodeprev = node.prev
        nodenext = node.next_
        nodeprev.next_ = nodenext
        node.next_ = None
        node.prev = None
        nodenext.prev = nodeprev

        self.size -= 1

    def remove_value(self, value):
        node = self.find_node(value)
        if node:
            self.remove_node(node)

    def find_node(self, value):
        """

        :param value:
        :rtype: Node | None
        :return:
        """
        firstnode = self.head.next_

        while firstnode != self.tail:
            if firstnode.value == value:
                return firstnode

            firstnode = firstnode.next_
        return None

    def contains(self, value):
        return self.find_node(value) is not None

    def add_first(self, node: Node):
        if not node:
            return

        headnext = self.head.next_

        self.head.next_ = node
        node.next_ = headnext
        node.prev = self.head
        headnext.prev = node

        self.size += 1
