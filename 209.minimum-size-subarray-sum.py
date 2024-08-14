#
# @lc app=leetcode.cn id=209 lang=python3
# @lcpr version=30204
#
# [209] 长度最小的子数组
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        result = 0
        i = 0
        sum = 0
        for j in range(len(nums)):
            sum += nums[j]
            while sum >= target:
                if result == 0 :
                    result = j - i + 1
                else:
                    result = min(result, j - i + 1)
                sum -= nums[i]
                i += 1
        return result
# @lc code=end



#
# @lcpr case=start
# 7\n[2,3,1,2,4,3]\n
# @lcpr case=end

# @lcpr case=start
# 4\n[1,4,4]\n
# @lcpr case=end

# @lcpr case=start
# 11\n[1,1,1,1,1,1,1,1]\n
# @lcpr case=end

#

