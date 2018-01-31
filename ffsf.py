# -*- coding: utf-8 -*-
# @Time    : 2018/1/17 13:11
# @Author  : wadedy

def resverse_num(num):
    # 数字翻转，例如num=123，则return值为321
    count = 1
    result = 0
    while num > 10:
        remainder = num % 10
        result = (result+remainder)*10
        num = num / 10
    result = result + num
    return result

def list_merge(nums1, nums2):
    # l1,l2为2个有序的序列,将其合并成一个新的有序的序列
    """
           :type nums1: List[int]
           :type nums2: List[int]
           :rtype: float
           """
    result = []
    while nums1 and nums2:
        if nums1[0] < nums2[0]:
            result.append(nums1[0])
            nums1.remove(nums1[0])
        elif nums1[0] > nums2[0]:
            result.append(nums2[0])
            nums2.remove(nums2[0])
        else:
            result.append(nums2[0])
            result.append(nums2[0])
            nums1.remove(nums1[0])
            nums2.remove(nums2[0])
    while nums1:
        result.append(nums1[0])
        nums1.remove(nums1[0])
    while nums2:
        result.append(nums2[0])
        nums2.remove(nums2[0])
    return result

l1 = [1, 2, 3, 4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22]

l2 = [0, 6]
print list_merge(l1, l2)

