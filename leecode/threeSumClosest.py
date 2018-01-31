# -*- coding: utf-8 -*-
# @Time    : 2018/1/31 16:12
# @Author  : wadedy

"""
https://leetcode.com/problems/3sum-closest/description/
Given an array S of n integers, find three integers in S such that the sum is closest to a given number, target.
Return the sum of the three integers. You may assume that each input would have exactly one solution.
    For example, given array S = {-1 2 1 -4}, and target = 1.
    The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
"""


class Solution(object):

    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        nums_len = len(nums)
        diff = 65535
        for i in xrange(nums_len - 1):
            temp_i, temp_j = i + 1, nums_len - 1
            while temp_i < temp_j:
                sum = nums[i] + nums[temp_i] + nums[temp_j]
                temp = abs(sum - target)
                if temp < diff:
                    closeset = sum
                    diff = temp
                if sum < target:
                    temp_i += 1
                elif sum > target:
                    temp_j -= 1
                elif sum == target:
                    return target
        return closeset

if __name__ == "__main__":
    sol = Solution()
    nums = [-1, 1, 1, 0]
    target = -100
    print sol.threeSumClosest(nums, target)