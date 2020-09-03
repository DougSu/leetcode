'''
Author: your name
Date: 2020-09-03 15:22:52
LastEditTime: 2020-09-03 15:55:33
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: \undefinede:\leetcode\66.加一.py
'''
#
# @lc app=leetcode.cn id=66 lang=python3
#
# [66] 加一
#

# @lc code=start
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        res = 0
        for i in digits:
            res = res*10+i
        res = res+1
        ret = list(map(int,str(res)))
        return ret
# @lc code=end

