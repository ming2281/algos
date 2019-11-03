#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# date:        2019/11/3
# author:      he.zhiming
#

from __future__ import (absolute_import, unicode_literals)

from queue import Queue
from typing import Callable
from collections import deque

class Node:
    def __init__(self, value, left=None, right=None):
        """

        :param value:
        :param Node left:
        :param Node right:
        """

        self.value = value
        self.left = left
        self.right = right


class BinarySearchTree:
    def __init__(self):
        self.root = None  # type: Node
        self.size = 0

    def add(self, value):
        """向树中加入元素

        :param value:
        :return:
        """
        if self.root is None:
            self.root = Node(value)
            self.size += 1
        else:
            self._add(self.root, value)

    def _add(self, node: Node, value):
        """加入元素,假定根节点为node

        :param node:
        :param value:
        :return: 返回根
        """
        if node is None:
            self.size += 1
            return Node(value)

        if value < node.value:
            node.left = self._add(node.left, value)
        elif value > node.value:
            node.right = self._add(node.right, value)

        return node

    def _remove(self, node: Node, value):
        """删除某元素

        :param node:
        :param value:
        :return: 返回根
        """
        if node is None:
            return None

        if value < node.value:
            node.left = self._remove(node.left, value)
            return node
        elif value > node.value:
            node.right = self._remove(node.right, value)
            return node
        else:
            if node.left is None:
                right_node = node.right
                node.right = None
                self.size -= 1
                return right_node
            if node.right is None:
                left_node = node.left
                node.left = None
                self.size -= 1
                return left_node

            # 找到一个node的后继节点
            successor = self.minimum(node.right)
            # 删除后继, 剩下的根, 变成s的右子树
            successor.right = self.removeMin(node.right)
            # s的左子树,为node的左子书
            successor.left = node.left

            # 删除node
            node.left = None
            node.right = None

            # 返回根
            return successor

    def minimum(self, node: Node) -> Node:
        """node为根的最小值的位置

        :param node:
        :return:
        """
        if node.left is None:
            return node
        return self.minimum(node.left)

    def maximum(self, node: Node) -> Node:
        if node.right is None:
            return node
        return self.maximum(node.right)

    def removeMin(self, node) -> Node:
        """删除node为根的最小节点

        :param node:
        :return: 删除节点后新的根
        """
        if node.left is None:
            rightNode = node.right  # 右子树替换上
            node.right = None  # 删除node
            self.size -= 1
            return rightNode  # 新的根
        else:
            node.left = self.removeMin(node.left)
            return node  # 根仍然是node

    def removeMax(self, node: Node) -> Node:
        if node.right is None:
            leftNode = node.left
            node.left = None
            self.size -= 1
            return leftNode

        node.right = self.removeMax(node.right)
        return node

    def levelOrder(self, traverseFunc: Callable[[Node], None]):
        """

        :param traverseFunc:
        :return:
        """
        q = Queue()
        q.put(self.root)

        while not q.empty():
            cur = q.get() # type: Node

            traverseFunc(cur)

            if cur.left is not None:
                q.put(cur.left)
            if cur.right is not None:
                q.put(cur.right)

    def preOrder(self):
        s = deque()

        s.append(self.root)
        while len(s) > 0:
            cur = s.pop() # type: Node

            print(cur)

            if cur.right != None:
                s.append(cur.right)
            if cur.right != None:
                s.append(cur.left)


    def inOrder(self):
        cur = self.root
        res = []
        s = deque()
        cur = self.root
        while cur != None or (len(s) > 0):
            if cur != None:
                s.append(cur)
                cur = cur.left
            else:
                cur = s.pop()
                res.append(cur.value)
                cur = cur.right

        return res

    def postOrder(self):
        s = deque()
        cur = self.root

        while cur != None or (len(s) > 0):
            if cur != None:
                s.append(cur)
                cur = cur.left
            else:
                cur = s.pop()
                if cur.right == None or pre


    def floor(self, value):
        """

        :return:
        """

    def ceil(self, value):
        """

        :return:
        """
