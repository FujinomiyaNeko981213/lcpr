#
# @lc app=leetcode.cn id=69 lang=python3
# @lcpr version=30204
#
# [69] x 的平方根 
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def mySqrt(self, x: int) -> int:
        left = 0
        right = x
        while left<= right:
            middle = (left + right) // 2
            if middle*middle>x:
                right = middle - 1
            elif middle*middle<x:
                left = middle + 1
            else:
                return middle
        return left - 1

# @lc code=end



#
# @lcpr case=start
# 4\n
# @lcpr case=end

# @lcpr case=start
# 8\n
# @lcpr case=end

#

