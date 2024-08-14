#
# @lc app=leetcode.cn id=904 lang=python3
# @lcpr version=30204
#
# [904] 水果成篮
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
from collections import Counter


class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        collec = Counter()
        ans = 0
        j = 0
        for i in range(len(fruits)):
            collec[fruits[i]] += 1
            while len(collec)>2:
                collec[fruits[j]] -= 1
                if collec[fruits[j]] == 0:
                    collec.pop(fruits[j])
                j+=1
            ans = max(ans, i - j + 1)
        return ans
            




# @lc code=end



#
# @lcpr case=start
# [1,2,1]\n
# @lcpr case=end

# @lcpr case=start
# [0,1,2,2]\n
# @lcpr case=end

# @lcpr case=start
# [1,2,3,2,2]\n
# @lcpr case=end

# @lcpr case=start
# [3,3,3,1,2,1,1,2,3,3,4]\n
# @lcpr case=end

#

