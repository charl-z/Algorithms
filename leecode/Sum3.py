# -*- coding: utf-8 -*-
# @Time    : 2018/1/30 13:09
# @Author  : wadedy

"""
https://leetcode.com/problems/3sum/description/
Given an array S of n integers, are there elements a, b, c in S such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.
Note: The solution set must not contain duplicate triplets.
For example, given array S = [-1, 0, 1, 2, -1, -4],
A solution set is:
[
  [-1, 0, 1],
  [-1, -1, 2]
]
"""


class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        #nums.sort()
        nums_len = len(nums)
        res = []
        for i in xrange(nums_len-2):
            for j in xrange(i+1, nums_len-1):
                temp_i, temp_j = j, nums_len-1
                while temp_i != temp_j:
                    if nums[i] + nums[temp_i] + nums[temp_j] == 0:
                        res.append([nums[i], nums[temp_i], nums[temp_j]])
                        temp_i += 1
                    else:
                        temp_j -= 1
        res_new = []
        for i in res:
            if i not in res_new:
                res_new.append(i)
        return res_new

class SolutionImprove(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        nums_len = len(nums)
        """使用set方法可以避免后面在对结果去重"""
        res = set()
        for i in xrange(nums_len-1):
            temp_i, temp_j = i+1, nums_len-1
            while temp_i < temp_j:
                sum = nums[i] + nums[temp_i] + nums[temp_j]
                if sum == 0:
                    res.add((nums[i], nums[temp_i], nums[temp_j]))
                    if nums[temp_j] == nums[temp_i]:
                        """
                        这是为了判断nums列表中所有的数字相同都为0这种情况，如果不加，LeetCode是判定超时的，
                        因为如果nums全为0，相当于所有的0都需要遍历，这是最差的情况，时间复杂度为o(n^2)
                        """
                        break
                    temp_i += 1
                    temp_j -= 1
                elif sum < 0:
                    """与未优化的代码相比，因为是有序的，所有只需要判定，如果sum<0，则只需要左边的向右移，否则右边的向左移"""
                    temp_i += 1
                else:
                    temp_j -= 1

        return list(res)




class Solution2(object):
    """
    leetcode上改进的代码，时间优化
    """
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums) < 3:
            return []
        nums.sort()
        s = set()
        for k, v in enumerate(nums):
            l, r = k+1, len(nums)-1
            while l < r:
                sums = v + nums[l] + nums[r]
                if sums == 0:
                    s.add((v, nums[l], nums[r]))
                    if nums[l] == nums[r]:
                        break
                    l += 1
                    r -= 1
                elif sums > 0:
                    r -= 1
                elif sums < 0:
                    l += 1
        return list(s)


class Solution3(object):
    def threeSum3(self, nums):
        counter = {}
        for num in nums:
            if num not in counter:
                counter[num] = 0
            counter[num] += 1

        if 0 in counter and counter[0] > 2:
            rst = [[0, 0, 0]]
        else:
            rst = []

        uniques = counter.keys()  # 它使用hash table来过滤重复数字

        pos = sorted(p for p in uniques if p > 0)  # 我只利用了将数组排列这一特征
        neg = sorted(n for n in uniques if n < 0)

        # 我也采取了分组(正数和负数)这一特征
        for p in pos:
            for n in neg:
                inverse = -(p + n)  # 通过设置sub-goal来设置
                if inverse in counter:
                    if inverse == p and counter[p] > 1:
                        rst.append([n, p, p])
                    elif inverse == n and counter[n] > 1:
                        rst.append([n, n, p])
                    elif (not n <= inverse <= p) or inverse == 0:
                        rst.append([n, inverse, p])
        return rst


'''
class Solution(object):
    def threeSum(self, nums):
        triplets = []
        if len(nums) < 3:
            return triplets
        nums.sort()
        for i in range(len(nums)):
            if i and nums[i] == nums[i - 1]:
                continue
            if nums[i] > 0:
                return triplets
            target = - nums[i]
            left, right = i + 1, len(nums) - 1
            while (left < right):
                if nums[left] + nums[right] == target:
                    triplets.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1
                elif nums[left] + nums[right] > target:
                    right -= 1
                else:
                    left += 1
        return triplets
'''

if __name__ == "__main__":
    # sol = Solution()
    #sol2 = Solution2()
    solim = SolutionImprove()
    nums = [0,-4,-1,-4,-2,-3,2]
    #print sol.threeSum(nums)
    #print sol2.threeSum(nums)
    print solim.threeSum(nums)





