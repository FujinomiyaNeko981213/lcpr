#
# @lc app=leetcode.cn id=844 lang=python3
# @lcpr version=30204
#
# [844] 比较含退格的字符串
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        s = list(s)
        t = list(t)
        slow = 0
        for i in s:
            if i !='#':
                s[slow]=i
                slow+=1
            else:
                if slow > 0:
                    slow-=1
        s = s[:slow]
        slow = 0
        for i in t:
            if i !='#':
                t[slow]=i
                slow+=1
            else:
                if slow > 0:
                    slow-=1
        t = t[:slow]
        return t==s

# @lc code=end



#
# @lcpr case=start
# "ab#c"\n"ad#c"\n
# @lcpr case=end

# @lcpr case=start
# "ab##"\n"c#d#"\n
# @lcpr case=end

# @lcpr case=start
# "a#c"\n"b"\n
# @lcpr case=end

#

