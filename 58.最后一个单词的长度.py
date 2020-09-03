'''
Author: your name
Date: 2020-09-02 17:59:07
LastEditTime: 2020-09-03 15:12:47
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: \undefinede:\leetcode\58.最后一个单词的长度.py
'''
#
# @lc app=leetcode.cn id=58 lang=python3
#
# [58] 最后一个单词的长度
#

# @lc code=start
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        # res = s.strip()
        # res = res.split(' ')
        # print(res)
        # return len(res[-1])
        e = len(s)-1
        star = e
        while e>=0 and s[e] ==" ":
            e = e-1
            star = e
        while star>=0 and s[star]!=" ":
            star = star-1
        print(e,star)
        return e-star
        
# @lc code=end

