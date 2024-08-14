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
from collections import defaultdict
class Solution:
    def compare_dicts(self, a, b):
        for key in a:
            if key not in b:
                return False
            if a[key] > b[key]:
                return False
        return True

    def minWindow(self, s: str, t: str) -> str:
        count_t = defaultdict(int)
        count_s = defaultdict(int)
        s = list(s)
        t = list(t)
        min_length = 0
        min_i, min_j = 0,-1
        for flag in range(len(t)):
            count_t[t[flag]] +=1
        i = 0
        for j in range(len(s)):
            count_s[s[j]] +=1
            while self.compare_dicts(count_t, count_s):
                if min_length == 0 or min_length > (j - i + 1):
                    min_length = j - i + 1
                    min_i, min_j = i, j
                count_s[s[i]] -= 1
                i += 1
        return ''.join(map(str, s[min_i:min_j + 1]))




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

