# @lcpr-before-debug-begin
from python3problem76 import *
from typing import *
# @lcpr-before-debug-end

#
# @lc app=leetcode.cn id=76 lang=python3
# @lcpr version=30204
#
# [76] 最小覆盖子串
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
# 1.使用Counter
# 2.初始化min_i,min_j应该使用不在范围内的值
# 3.当符合条件时，先更新结果，再更新用于比较的counter
# 4.因为j指向终端，i指向开始，在寻找最小区间时，永远是i++
from collections import Counter
class Solution:
    def compare_dict(self, dict1, dict2) -> bool:
        for key in dict1:
            if dict2[key] == 0 or dict2[key] < dict1[key]:
                return False
        return True


    def minWindow(self, s: str, t: str) -> str:
        s = list(s)
        t = list(t)
        dict_t = Counter()
        dict_s = Counter()
        for i in t:
            dict_t[i]+=1
        min_i = -1
        min_j = -1
        i = 0
        for j in range(len(s)):
            dict_s[s[j]] +=1
            while self.compare_dict(dict_t, dict_s):
                if (min_i == -1 and min_j == -1) or ((min_j- min_i) > (j - i)):
                    min_i, min_j = i,j
                dict_s[s[i]] -= 1
                i +=1
        if min_i == -1 and min_j == -1:
            return ''
        return ''.join(s[min_i:min_j+1])




# @lc code=end



#
# @lcpr case=start
# "ADOBECODEBANC"\n"ABC"\n
# @lcpr case=end

# @lcpr case=start
# "a"\n"a"\n
# @lcpr case=end

# @lcpr case=start
# "a"\n"aa"\n
# @lcpr case=end

# @lcpr case=start
# "cabwefgewcwaefgcf"\n"cae"\n
# @lcpr case=end

