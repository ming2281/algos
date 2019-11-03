#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# date:        2019/11/2
# author:      he.zhiming
#

from __future__ import (absolute_import, unicode_literals)

from typing import Optional


class Node:
    def __init__(self, key: int, value: int, prev=None, next_=None):
        """

        :param key:
        :param value:
        :type prev: Node
        :param prev:
        :type next_: Node
        :param next_:
        """
        self.key = key
        self.value = value
        self.prev = prev
        self.next = next_


class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.size = 0
        self.key_node = {}  # type: dict[int, Node]

        self.head = Node(None, None)
        self.head.prev = None
        self.tail = Node(None, None)
        self.tail.next = None
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        node = self.key_node.get(key)

        if node is None:
            return -1
        else:
            # 存在
            # 移动到头部
            self.move_to_head(node)

            return node.value

    def put(self, key: int, value: int) -> None:
        node = self.key_node.get(key)

        if node is None:
            # 不存在，放进去
            newnode = Node(key, value)

            # 移动到头部
            self.move_to_head(newnode)
            self.size += 1

            # size判断，删除尾巴
            if self.size > self.cap:
                self.remove_tail()
                self.size -= 1

            self.key_node[key] = newnode

        else:
            # 移动到头部
            self.move_to_head(node)

    def move_to_head(self, node: Node) -> None:
        """

        :param node:
        :return:
        """
        if node and (node.prev == self.head):
            return

        if node:
            headnext = self.head.next
            self.head.next = node
            node.next = headnext
            node.prev = self.head
            headnext.prev = node

    def remove_tail(self):
        """
        :rtype: Node|None
        :return:
        """
        node = self.tail.prev

        if node == self.head:
            return None

        if node:
            prev = node.prev

            prev.next = self.tail
            node.next = None
            node.prev = None
            self.tail.prev = prev

        return node

    def print_list(self):
        first = self.head.next

        values = []
        while first and first != self.tail:
            values.append(first.value)

            first = first.next

        print(values)

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
