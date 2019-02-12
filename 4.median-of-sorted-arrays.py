#
# @lc app=leetcode.cn id=4 lang=python3
#
# [4] 寻找两个有序数组的中位数
#
# https://leetcode-cn.com/problems/median-of-two-sorted-arrays/description/
#
# algorithms
# Hard (32.86%)
# Total Accepted:    32.2K
# Total Submissions: 98.1K
# Testcase Example:  '[1,3]\n[2]'
#
# 给定两个大小为 m 和 n 的有序数组 nums1 和 nums2。
#
# 请你找出这两个有序数组的中位数，并且要求算法的时间复杂度为 O(log(m + n))。
#
# 你可以假设 nums1 和 nums2 不会同时为空。
#
# 示例 1:
#
# nums1 = [1, 3]
# nums2 = [2]
#
# 则中位数是 2.0
#
#
# 示例 2:
#
# nums1 = [1, 2]
# nums2 = [3, 4]
#
# 则中位数是 (2 + 3)/2 = 2.5
#
#
#
class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        A = nums1 if len(nums1) < len(nums2) else nums2
        B = nums2 if len(nums1) < len(nums1) else nums1
        m = len(A)
        n = len(B)
        iMin = 0
        iMax = m
        while True:
            i = (iMin + iMax) // 2
            j = (m + n + 1) // 2 - i
            if i <= 0 or A[i - 1] <= B[j] and i >= m or B[j - 1] <= A[i]:
                break
            elif A[i] < B[j - 1]:
                iMin = i + 1
            else:
                iMax = i - 1

        if (m + n) % 2 == 0:
            if i <= 0:
                maxLeft = B[j - 1]
            elif j <= 0:
                maxLeft = A[i - 1]
            else:
                maxLeft = max(A[i - 1], B[j - 1])
            if i >= m:
                minRight = B[j]
            elif j >= n:
                minRight = A[i]
            else:
                minRight = min(A[i], B[j])
            return (maxLeft + minRight) / 2.0
        else:
            maxLeft = B[j - 1] if i == 0 else max(A[i - 1], B[j - 1])
            return maxLeft
