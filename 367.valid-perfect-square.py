#
# @lc app=leetcode.cn id=367 lang=python3
# @lcpr version=30204
#
# [367] 有效的完全平方数
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        left = 0
        right = num // 2 + 1
        while left <= right:
            middle = (left + right) // 2
            if middle*middle> num:
                right = middle -1
            elif middle*middle<num:
                left = middle + 1
            else:
                return True
        return False
# @lc code=end



#
# @lcpr case=start
# 16\n
# @lcpr case=end

# @lcpr case=start
# 14\n
# @lcpr case=end

#

