#
# @lc app=leetcode.cn id=21 lang=python3
#
# [21] 合并两个有序链表
#
# https://leetcode-cn.com/problems/merge-two-sorted-lists/description/
#
# algorithms
# Easy (51.70%)
# Total Accepted:    40K
# Total Submissions: 77.2K
# Testcase Example:  '[1,2,4]\n[1,3,4]'
#
# 将两个有序链表合并为一个新的有序链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。 
#
# 示例：
#
# 输入：1->2->4, 1->3->4
# 输出：1->1->2->3->4->4
#
#
#
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        new_list = ListNode(0)
        p = new_list
        # 谁小先挂谁的结点
        while l1 and l2:
            if l1.val <= l2.val:
                p.next = l1
                p = p.next
                l1 = l1.next

            else:
                p.next = l2
                p = p.next
                l2 = l2.next
        # 肯定有一个链表先挂完，把剩余的挂上
        if l1:
            p.next = l1
        else:
            p.next = l2
        return new_list.next


l1 = [1, 2, 4]
l2 = [1, 3, 4]
s = Solution()
print(s.mergeTwoLists(ListNode(l1), ListNode(l2)))