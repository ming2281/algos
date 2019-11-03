#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# date:        2019/10/27
# author:      he.zhiming
#

from __future__ import (absolute_import, unicode_literals)

from algos.utils import make_length_list


def merge_sort(arr):
    """

    :param arr:
    :return:
    """
    if not arr or (len(arr) <= 1):
        return arr

    _merge_sort(arr, 0, len(arr) - 1)


def _merge_sort(arr, left, right):
    """ [left, right]

    :param arr:
    :param left:
    :param right:
    :return:
    """
    if left >= right:
        return

    mid = (left + right) // 2
    # 排左边, 区间大小, 要一直符合定义
    _merge_sort(arr, left, mid)
    # 排右边, 区间大小, 要一直符合定义
    _merge_sort(arr, mid + 1, right)

    # 归并, 注意: 区间取值
    _merge(arr, left, mid, right)


def  _merge(arr, l, mid, r):
    """
    [left, mid]

    [mid+1, right]

    :param arr:
    :param l:
    :param mid:
    :param r:
    :return:
    """
    # 使用一个辅助数据,将arr里面的内容全部放进去
    aux = make_length_list(r - l + 1)  # 大小: r-l+1
    for i in range(l, r + 1):  # i取值: [l, r]
        aux[i - l] = arr[l]

    # i: 左边那个数组   j: 右边那个数组  k: 开始位置(arr) [l...r]
    i = l
    j = mid + 1
    k = l
    while k <= r:
        if i > mid:
            arr[k] = aux[j - l]
            j += 1
        elif j > r:
            arr[k] = aux[i - l]
            i += 1
        else:
            if aux[i - l] < aux[j - l]:
                arr[k] = aux[i - l]
                i += 1
            else:
                arr[k] = aux[j - l]
                j += 1
        k += 1
