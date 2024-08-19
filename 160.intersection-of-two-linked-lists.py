#
# @lc app=leetcode.cn id=160 lang=python3
# @lcpr version=30204
#
# [160] 相交链表
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        current = ListNode(0)
        current.next = headA
        count_A = 0
        while current.next!=None:
            current = current.next
            count_A +=1
        current = ListNode(0)
        current.next = headB
        count_B = 0
        while current.next!=None:
            current = current.next
            count_B +=1
        diff = count_A-count_B
        current_A = headA
        current_B = headB
        if diff>=0:
            while diff:
                current_A = current_A.next
                diff -= 1
            
        else:
            diff = abs(diff)
            while diff:
                current_B = current_B.next
                diff -= 1
        while current_A !=None and current_B!=None:
            if current_A == current_B:
                return current_B
            else:
                current_A = current_A.next
                current_B = current_B.next



# @lc code=end



#
# @lcpr case=start
# 8\n[4,1,8,4,5]\n[5,6,1,8,4,5]\n2\n3\n
# @lcpr case=end

# @lcpr case=start
# 2\n[1,9,1,2,4]\n[3,2,4]\n3\n1\n
# @lcpr case=end

# @lcpr case=start
# 0\n[2,6,4]\n[1,5]\n3\n2\n
# @lcpr case=end

#

